# Purelane → Shopify Step-by-Step Setup & QA Guide

Follow these sequential steps to set up, test, and verify the Purelane theme sections on your Shopify Development Store before submitting your assignment.

---

## Phase 1: Product Catalog Seeding (Shopify Admin)

1. Navigate to **Shopify Admin > Products**.
2. Click **Import** in the top right header.
3. Select **Upload a Shopify-formatted CSV file** and click **Next**.
4. Click **Add file** and select the seed CSV file from your project:
   - Path: [`data/seed-products.csv`](file:///C:/Users/jegad/projects/TroopodAIEngineer/data/seed-products.csv)
5. *(Optional)* Check **"Overwrite any current products that have the same handle"**.
6. Click **Upload and preview**, then click **Import products**.
7. **Verify Edge Cases in Admin:**
   - [ ] **Sold Out Edge Case:** Verify `Eco Multi-Surface Floor Cleaner Super Concentrate Formula` has inventory set to `0`.
   - [ ] **No Image Edge Case:** Verify `Purelane Plant-Powered Glass & Mirror Cleaner Refill` has no image (tests inline SVG placeholder fallback).
   - [ ] **Long Title Edge Case:** Verify `Purelane Ultra-Concentrated Plant-Based Liquid Laundry Detergent...` title exceeds 80 characters (tests 2-line clamping).

---

## Phase 2: Product Metafield Setup (Shopify Admin)

Navigate to **Shopify Admin > Settings > Custom Data > Products > Add definition** and create the following 5 metafield definitions matching [`metafields/schema-definitions.json`](file:///C:/Users/jegad/projects/TroopodAIEngineer/metafields/schema-definitions.json):

| Definition Name | Namespace and Key | Type | Description |
|---|---|---|---|
| Rating Score | `custom.rating_score` | Decimal number | Rating out of 5 (e.g., `4.8`) |
| Review Count | `custom.review_count` | Integer | Total review count (e.g., `1420`) |
| Badge Text | `custom.badge_text` | Single line text | Product card pill badge (e.g., `"Bestseller"`) |
| Benefit Tag | `custom.benefit_tag` | Single line text | Card tagline (e.g., `"Cuts grease naturally"`) |
| Combo Products | `custom.combo_products` | List of Product references | Referenced products in bundle |

---

## Phase 3: Theme Code Deployment

Choose **Option A** or **Option B**:

### Option A: Shopify CLI (Recommended)
1. Open PowerShell / Terminal in your workspace root.
2. Run:
   ```bash
   shopify theme dev --path shopify
   ```
3. Open the generated preview URL in your browser.

### Option B: Manual Theme Upload
1. Compress the contents of the `shopify/` folder into a `.zip` archive.
2. Go to **Shopify Admin > Online Store > Themes > Add Theme > Upload zip file**.
3. Select your `.zip` archive and click **Actions > Customize**.

---

## Phase 4: Theme Customizer Setup (Section Configuration)

In the Shopify Theme Editor (Customizer), add and configure the 5 Purelane sections onto your Homepage:

1. **Section 01: Purelane Hero** ([`shopify/sections/purelane-hero.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/sections/purelane-hero.liquid))
   - Configure main headline, subtext, primary CTA ("Shop Best Sellers"), and secondary CTA ("Explore Combos").
   - Add up to 3 Hero Product Slide blocks and assign products.

2. **Section 02: Purelane Shop Grid** ([`shopify/sections/purelane-shop-grid.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/sections/purelane-shop-grid.liquid))
   - Select the collection containing your 8 imported seed products.
   - Set products limit to `8`.
   - Verify card rendering uses [`shopify/snippets/purelane-product-card.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/snippets/purelane-product-card.liquid).

3. **Section 03: Purelane Combos** ([`shopify/sections/purelane-combos.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/sections/purelane-combos.liquid))
   - Add Combo Card blocks and bind product references and benefit tags.
   - Verify card rendering uses [`shopify/snippets/purelane-combo-card.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/snippets/purelane-combo-card.liquid).

4. **Section 04: Purelane Bundles** ([`shopify/sections/purelane-bundles.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/sections/purelane-bundles.liquid))
   - Add 3 Bundle Tier blocks (e.g., 2 Bottle Starter, 3 Bottle Complete, 5 Bottle Total Clean).
   - Set the 3 Bottle tier as **Featured** to test primary highlight styling (`btn-primary`).

5. **Section 05: Purelane Reviews** ([`shopify/sections/purelane-reviews.liquid`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/sections/purelane-reviews.liquid))
   - Set aggregate rating score (e.g., `4.9`) and review count text.
   - Add Review Card blocks to populate the marquee.

---

## Phase 5: Manual QA & Behavior Verification

Perform the following manual test checks on the live preview site:

- [ ] **Responsive Design:** Resize viewport from 375px (mobile) up to 1440px+ to ensure zero horizontal scroll overflow.
- [ ] **AJAX Add to Cart:** Click "Add to Cart" on a product card; confirm the item is added via AJAX without a full page refresh.
- [ ] **Multi-Item Cart Dispatch:** Click "Add Combo to Cart" or "Build Bundle"; inspect Network tab to verify POST to `/cart/add.js` sends multi-item JSON array payloads.
- [ ] **Sold Out State:** Check the sold out item (`Eco Multi-Surface Floor Cleaner`); confirm button reads "Sold Out" and is disabled.
- [ ] **Missing Image Fallback:** Check `Purelane Plant-Powered Glass & Mirror Cleaner Refill`; confirm inline SVG branded bottle placeholder renders cleanly.
- [ ] **Title Line Clamping:** Check the long title detergent product; confirm title clamps to 2 lines max without breaking grid row heights.
- [ ] **Theme Editor Resilience:** In Customizer, reorder or add/remove sections. Confirm slideshows and marquee animations re-initialize without JS errors (driven by `shopify:section:load` in [`shopify/assets/purelane-scripts.js`](file:///C:/Users/jegad/projects/TroopodAIEngineer/shopify/assets/purelane-scripts.js)).
- [ ] **Accessibility:** Enable "Reduce Motion" in system settings or browser DevTools; confirm animations disable instantly. Test keyboard navigation using `Tab` key to verify visible focus outlines (`:focus-visible`).

---

## Phase 6: Final Submission Checklist

Send an email to **`nj@troopod.io`** with the subject:
`AI Product Engineer Assignment - Your Name`

Include the following items:
1. **Development Store URL** (e.g., `https://your-store.myshopify.com`)
2. **Store Front Password** (Found under **Online Store > Preferences > Password protection**)
3. **GitHub Repository URL** (with full commit history)
4. Reference to created files:
   - [`metafields/schema-definitions.json`](file:///C:/Users/jegad/projects/TroopodAIEngineer/metafields/schema-definitions.json)
   - [`docs/build-notes.md`](file:///C:/Users/jegad/projects/TroopodAIEngineer/docs/build-notes.md)
   - [`docs/ai-workflow-notes.md`](file:///C:/Users/jegad/projects/TroopodAIEngineer/docs/ai-workflow-notes.md)
