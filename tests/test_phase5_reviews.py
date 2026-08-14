import os
import json
import re
import unittest

class TestPhase5Reviews(unittest.TestCase):

    def setUp(self):
        reviews_path = os.path.join(os.getcwd(), "shopify/sections/purelane-reviews.liquid")
        with open(reviews_path, encoding="utf-8") as fh:
            self.reviews_liquid = fh.read()

        css_path = os.path.join(os.getcwd(), "shopify/assets/purelane-styles.css")
        with open(css_path, encoding="utf-8") as fh:
            self.css = fh.read()

    def test_reviews_has_marquee_track(self):
        self.assertIn("revtrack", self.reviews_liquid)

    def test_reviews_duplicates_track_for_seamless_scroll(self):
        count = self.reviews_liquid.count("revtrack")
        self.assertGreaterEqual(count, 2, "Marquee track must be duplicated for seamless loop")

    def test_reviews_has_aria_labels(self):
        self.assertIn("aria-label", self.reviews_liquid)
        self.assertIn("aria-hidden", self.reviews_liquid)

    def test_reviews_speed_from_settings(self):
        self.assertTrue("section.settings.marquee_speed" in self.reviews_liquid or "--duration" in self.reviews_liquid)

    def test_reviews_schema_has_review_block(self):
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', self.reviews_liquid, re.DOTALL)
        self.assertIsNotNone(schema_match)
        schema = json.loads(schema_match.group(1))
        block_types = [b["type"] for b in schema.get("blocks", [])]
        self.assertIn("review_card", block_types)

    def test_reviews_reduced_motion_stops_animation(self):
        self.assertIn("prefers-reduced-motion", self.css)

if __name__ == "__main__":
    unittest.main()
