import os
import json
import re
import unittest

class TestPhase2ShopGrid(unittest.TestCase):

    def setUp(self):
        shop_path = os.path.join(os.getcwd(), "shopify/sections/purelane-shop-grid.liquid")
        with open(shop_path, encoding="utf-8") as fh:
            self.shop_liquid = fh.read()

        card_path = os.path.join(os.getcwd(), "shopify/snippets/purelane-product-card.liquid")
        with open(card_path, encoding="utf-8") as fh:
            self.card_liquid = fh.read()

    def test_shop_uses_collection_loop(self):
        self.assertIn("selected_collection.products", self.shop_liquid)

    def test_shop_respects_limit(self):
        self.assertIn("limit:", self.shop_liquid)

    def test_shop_renders_card_snippet(self):
        self.assertIn("purelane-product-card", self.shop_liquid)

    def test_shop_schema_has_collection_picker(self):
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', self.shop_liquid, re.DOTALL)
        self.assertIsNotNone(schema_match)
        schema = json.loads(schema_match.group(1))
        setting_types = [s["type"] for s in schema.get("settings", [])]
        self.assertIn("collection", setting_types)

    def test_product_card_snippet_handles_no_image(self):
        self.assertTrue("product.featured_image" in self.card_liquid)
        self.assertIn("<svg", self.card_liquid)

    def test_product_card_snippet_handles_sold_out(self):
        self.assertIn("available", self.card_liquid)
        self.assertIn("disabled", self.card_liquid)
        self.assertIn("Sold out", self.card_liquid)

    def test_product_card_snippet_clamps_long_title(self):
        self.assertIn("line-clamp", self.card_liquid)

if __name__ == "__main__":
    unittest.main()
