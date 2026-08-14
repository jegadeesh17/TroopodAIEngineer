import os
import json
import unittest

REQUIRED_FILES = [
    "SPEC.md",
    "shopify/assets/purelane-styles.css",
    "shopify/assets/purelane-scripts.js",
    "shopify/snippets/purelane-product-card.liquid",
    "shopify/snippets/purelane-combo-card.liquid",
    "data/seed-products.json",
    "metafields/schema-definitions.json",
]

class TestPhase0Spec(unittest.TestCase):

    def test_required_files_exist(self):
        for f in REQUIRED_FILES:
            path = os.path.join(os.getcwd(), f)
            self.assertTrue(os.path.exists(path), f"Missing required file: {f}")

    def test_seed_products_valid_json(self):
        seed_path = os.path.join(os.getcwd(), "data/seed-products.json")
        with open(seed_path, encoding="utf-8") as fh:
            data = json.load(fh)
        self.assertEqual(len(data["products"]), 8, "Must have 8 seed products")
        
        # Edge case 1: Sold out product
        self.assertTrue(any(p.get("inventory_quantity") == 0 for p in data["products"]), "Must have a sold out product")
        # Edge case 2: No image product
        self.assertTrue(any(not p.get("images") for p in data["products"]), "Must have a product without images")
        # Edge case 3: Long title product
        self.assertTrue(any(len(p["title"]) > 80 for p in data["products"]), "Must have a long-title product")

    def test_metafield_schema_valid(self):
        schema_path = os.path.join(os.getcwd(), "metafields/schema-definitions.json")
        with open(schema_path, encoding="utf-8") as fh:
            data = json.load(fh)
        keys = [d["key"] for d in data]
        for required in ["rating_score", "review_count", "badge_text", "benefit_tag", "combo_products"]:
            self.assertIn(required, keys, f"Missing metafield key: {required}")

if __name__ == "__main__":
    unittest.main()
