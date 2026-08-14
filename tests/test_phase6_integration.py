import os
import json
import re
import unittest

SECTIONS = [
    "shopify/sections/purelane-hero.liquid",
    "shopify/sections/purelane-shop-grid.liquid",
    "shopify/sections/purelane-combos.liquid",
    "shopify/sections/purelane-bundles.liquid",
    "shopify/sections/purelane-reviews.liquid",
]

class TestPhase6Integration(unittest.TestCase):

    def test_all_sections_exist(self):
        for s in SECTIONS:
            path = os.path.join(os.getcwd(), s)
            self.assertTrue(os.path.exists(path), f"Section file missing: {s}")

    def test_all_sections_have_valid_schemas(self):
        for s in SECTIONS:
            path = os.path.join(os.getcwd(), s)
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
            schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
            self.assertIsNotNone(schema_match, f"No schema block found in {s}")
            try:
                schema = json.loads(schema_match.group(1))
            except Exception as e:
                self.fail(f"Invalid JSON schema in {s}: {e}")
            self.assertIn("name", schema, f"Schema missing name in {s}")
            self.assertTrue("settings" in schema or "blocks" in schema, f"Schema missing settings/blocks in {s}")

    def test_theme_editor_event_listeners(self):
        js_path = os.path.join(os.getcwd(), "shopify/assets/purelane-scripts.js")
        with open(js_path, encoding="utf-8") as fh:
            js_content = fh.read()
        self.assertIn("shopify:section:load", js_content)

    def test_accessibility_reduced_motion(self):
        css_path = os.path.join(os.getcwd(), "shopify/assets/purelane-styles.css")
        with open(css_path, encoding="utf-8") as fh:
            css_content = fh.read()
        self.assertIn("prefers-reduced-motion", css_content)

if __name__ == "__main__":
    unittest.main()
