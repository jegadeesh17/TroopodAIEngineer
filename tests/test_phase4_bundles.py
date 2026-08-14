import os
import json
import re
import unittest

class TestPhase4Bundles(unittest.TestCase):

    def setUp(self):
        bundles_path = os.path.join(os.getcwd(), "shopify/sections/purelane-bundles.liquid")
        with open(bundles_path, encoding="utf-8") as fh:
            self.bundles_liquid = fh.read()

    def test_bundles_uses_section_blocks(self):
        self.assertIn("section.blocks", self.bundles_liquid)

    def test_bundles_has_featured_variant(self):
        self.assertIn("is_featured", self.bundles_liquid)
        self.assertIn("btn-primary", self.bundles_liquid)
        self.assertIn("btn-ghost", self.bundles_liquid)

    def test_bundles_schema_has_tier_block(self):
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', self.bundles_liquid, re.DOTALL)
        self.assertIsNotNone(schema_match)
        schema = json.loads(schema_match.group(1))
        block_types = [b["type"] for b in schema.get("blocks", [])]
        self.assertIn("bundle_tier", block_types)

    def test_bundles_feature_list_is_dynamic(self):
        self.assertIn("block.settings.feature_1", self.bundles_liquid)

    def test_bundles_price_from_settings(self):
        self.assertIn("block.settings.price", self.bundles_liquid)
        self.assertIn("block.settings.compare_price", self.bundles_liquid)

if __name__ == "__main__":
    unittest.main()
