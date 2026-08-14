import os
import json
import re
import unittest

class TestPhase1Hero(unittest.TestCase):

    def setUp(self):
        hero_path = os.path.join(os.getcwd(), "shopify/sections/purelane-hero.liquid")
        with open(hero_path, encoding="utf-8") as fh:
            self.hero_liquid = fh.read()

    def test_hero_section_class(self):
        self.assertTrue('class="hero' in self.hero_liquid or "class='hero" in self.hero_liquid)

    def test_hero_has_h1(self):
        self.assertIn("<h1", self.hero_liquid)

    def test_hero_has_schema(self):
        self.assertIn("{% schema %}", self.hero_liquid)

    def test_hero_schema_has_blocks(self):
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', self.hero_liquid, re.DOTALL)
        self.assertIsNotNone(schema_match, "No schema block found")
        schema = json.loads(schema_match.group(1))
        block_types = [b["type"] for b in schema.get("blocks", [])]
        self.assertIn("hero_slide", block_types)

    def test_hero_no_hardcoded_prices(self):
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', self.hero_liquid, re.DOTALL)
        schema_text = schema_match.group(1) if schema_match else ""
        raw_prices = re.findall(r'₹\d+(?!</)', self.hero_liquid)
        for p in raw_prices:
            self.assertIn(p, schema_text, f"Hardcoded price {p} found outside schema")

if __name__ == "__main__":
    unittest.main()
