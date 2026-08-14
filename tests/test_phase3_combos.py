import os
import json
import re
import unittest

class TestPhase3Combos(unittest.TestCase):

    def setUp(self):
        combos_path = os.path.join(os.getcwd(), "shopify/sections/purelane-combos.liquid")
        with open(combos_path, encoding="utf-8") as fh:
            self.combos_liquid = fh.read()

        snippet_path = os.path.join(os.getcwd(), "shopify/snippets/purelane-combo-card.liquid")
        with open(snippet_path, encoding="utf-8") as fh:
            self.snippet_liquid = fh.read()

    def test_combos_uses_section_blocks(self):
        self.assertIn("section.blocks", self.combos_liquid)

    def test_combos_renders_combo_snippet(self):
        self.assertIn("purelane-combo-card", self.combos_liquid)

    def test_combos_schema_has_combo_block(self):
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', self.combos_liquid, re.DOTALL)
        self.assertIsNotNone(schema_match)
        schema = json.loads(schema_match.group(1))
        block_types = [b["type"] for b in schema.get("blocks", [])]
        self.assertIn("combo_card", block_types)

    def test_combo_card_snippet_has_block_id(self):
        self.assertIn("block.id", self.snippet_liquid)

    def test_combo_card_snippet_has_ajax_cart(self):
        self.assertTrue("cart/add" in self.snippet_liquid or "purelane-ajax-form" in self.snippet_liquid)

    def test_combo_card_handles_missing_products(self):
        self.assertIn("block.settings.product_1", self.snippet_liquid)

if __name__ == "__main__":
    unittest.main()
