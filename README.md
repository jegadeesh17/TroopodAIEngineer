# Purelane → Production Shopify Dawn Sections
### **AI Product Engineer Build Assignment — Troopod**

[![Test Suite](https://img.shields.io/badge/Tests-36%2F36%20Passed-brightgreen)](tests/)
[![Shopify Theme](https://img.shields.io/badge/Shopify%20Dawn-15.2.0-blue)](shopify/)
[![Code Style](https://img.shields.io/badge/Architecture-Clean%20Liquid%20%26%20CSS-purple)](shopify/assets/purelane-styles.css)

---

## **1. Project Overview**

This repository contains the complete production implementation converting the `purelane-homepage.html` prototype into **5 merchant-editable Shopify Dawn Liquid sections**. Built natively for stock Dawn with zero third-party framework dependencies, pixel-accurate fidelity, full theme-editor resilience, multi-item AJAX cart integration, and comprehensive automated test coverage.

---

## **2. Live Dev Store Access & Deliverables**

| Deliverable Item | Value / Link |
|---|---|
| **Live Storefront URL** | [https://purelane-b6xmmy8v.myshopify.com](https://purelane-b6xmmy8v.myshopify.com) |
| **Theme Preview URL** | [https://purelane-b6xmmy8v.myshopify.com?preview_theme_id=149257551951](https://purelane-b6xmmy8v.myshopify.com?preview_theme_id=149257551951) |
| **Storefront Password** | `yiefra` |
| **GitHub Repository** | [https://github.com/jegadeesh17/TroopodAIEngineer](https://github.com/jegadeesh17/TroopodAIEngineer) |
| **Metafields Schema** | [`metafields/schema-definitions.json`](metafields/schema-definitions.json) |
| **Product Seed Data** | [`data/seed-products.csv`](data/seed-products.csv) & [`data/seed-products.json`](data/seed-products.json) |
| **Step-by-Step Setup & QA Guide** | [`SETUP_AND_QA_GUIDE.md`](SETUP_AND_QA_GUIDE.md) |
| **Build & Architecture Notes** | [`docs/build-notes.md`](docs/build-notes.md) |
| **AI Workflow & Scaling Notes** | [`docs/ai-workflow-notes.md`](docs/ai-workflow-notes.md) |

---

## **3. Repository Structure**

```text
TroopodAIEngineer/
├── shopify/
│   ├── assets/
│   │   ├── purelane-styles.css          # Master CSS tokens, living background & glassmorphism
│   │   └── purelane-scripts.js          # Theme-editor safe JS (stage switcher & AJAX cart)
│   ├── layout/
│   │   └── theme.liquid                 # Injected living underwater #scenes & glass navpill
│   ├── sections/
│   │   ├── purelane-hero.liquid         # Section 01: Hero stage switcher & botanical badges
│   │   ├── purelane-shop-grid.liquid    # Section 02: Collection-bound product shelf
│   │   ├── purelane-combos.liquid       # Section 03: Swipeable combo bundle rail
│   │   ├── purelane-bundles.liquid      # Section 04: 3-tier pricing bundle cards
│   │   └── purelane-reviews.liquid      # Section 05: Auto-marquee customer review rail
│   └── snippets/
│       ├── purelane-product-card.liquid # Product card component (handles edge cases)
│       └── purelane-combo-card.liquid   # Combo card component (multi-item add to cart)
├── data/
│   ├── seed-products.csv                # Shopify-formatted product import CSV
│   └── seed-products.json               # Seed product catalog definitions
├── metafields/
│   └── schema-definitions.json          # 5 exportable Shopify metafield definitions
├── docs/
│   ├── purelane-homepage.html           # Original standalone design prototype
│   ├── build-notes.md                   # Prototype audit, architectural choices & fixes
│   └── ai-workflow-notes.md             # Agent delegation, failure modes & 20+ store scale
├── tests/                               # Automated test suite (Python unittest / pytest)
│   ├── test_phase0_spec.py
│   ├── test_phase1_hero.py
│   ├── test_phase2_shop_grid.py
│   ├── test_phase3_combos.py
│   ├── test_phase4_bundles.py
│   ├── test_phase5_reviews.py
│   └── test_phase6_integration.py
├── SETUP_AND_QA_GUIDE.md                # Merchant setup & manual QA checklist
├── SPEC.md                              # Master technical specification
├── requirements.txt                     # Test suite dependencies
└── README.md                            # Project documentation
```

---

## **4. Five Scoped Sections**

1. **Section 01: Hero (`purelane-hero.liquid`)**
   - 3-step interactive bottle stage switcher (`.hstage`, `.hp`, `.ptag`, `.hdots`) with auto-rotation.
   - Display typography (`Outfit` / `Inter`) with accent highlights.
   - Desktop botanical promise badges and responsive mobile badge strip.

2. **Section 02: Shop Product Grid (`purelane-shop-grid.liquid`)**
   - 4-column glass card grid (`.shelf .card.glass`) bound to collections with limit control.
   - Botanical SVG rule divider.
   - Two-line clamped titles, star ratings with review counts, discount percentage tags, and AJAX Add to Cart.
   - Robust edge cases: SVG bottle silhouettes for missing images and disabled state for sold-out products.

3. **Section 03: Best Selling Combos (`purelane-combos.liquid`)**
   - Horizontal swipeable scroll-snap rail (`.comborail`, `.combo.glass`).
   - Savings pill badges (`You save ₹398`), badges (`Most popular`, `Best value`), and product stacks with `+` dividers.
   - Dynamic CTA linking to `#bundles` or AJAX multi-item cart additions.

4. **Section 04: Build Your Bundle (`purelane-bundles.liquid`)**
   - 3-tier glass cards (`Starter`, `Most popular`, `Whole home`).
   - Product silhouette rows (`.tierpix`), large quantity callouts (`2`, `3`, `5 Products`), discount comparison pricing, and feature checklists.

5. **Section 05: Customer Reviews Marquee (`purelane-reviews.liquid`)**
   - Infinite marquee rail with duplicate track for seamless loops.
   - Aggregate score header (`★ 4.8 from 8,000+ reviews`).
   - Glass cards with star ratings, quotes, verified buyer indicators, and product tags.

---

## **5. Running Automated Tests**

Run the complete test suite locally across all section modules:

```powershell
python -m unittest discover -s tests
```

Or using `pytest`:

```powershell
pip install -r requirements.txt
pytest tests/ -v
```

Expected output:
```text
Ran 36 tests in 0.080s
OK (36/36 passed, 0 failures, 0 errors)
```
