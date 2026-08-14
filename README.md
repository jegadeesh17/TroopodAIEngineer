# Purelane → Production Shopify Dawn Sections
### **AI Product Engineer Build Assignment — Troopod**

---

### **Project Overview**

This repository contains the complete production implementation converting the `purelane-homepage.html` prototype into **5 merchant-editable Shopify Dawn Liquid sections**. Built natively for stock Dawn with zero third-party framework dependencies, pixel-accurate fidelity, full theme-editor resilience, multi-item AJAX cart integration, and comprehensive automated test coverage.

---

### **Repository Structure**

```text
TroopodAIEngineer/
├── shopify/
│   ├── assets/
│   │   ├── purelane-styles.css    # Extracted CSS system (design tokens, glassmorphism)
│   │   └── purelane-scripts.js    # Theme-editor safe JS (shopify:section:load re-init)
│   ├── sections/
│   │   ├── purelane-hero.liquid        # Section 01: Hero stage switcher & badges
│   │   ├── purelane-shop-grid.liquid   # Section 02: Collection-bound product grid
│   │   ├── purelane-combos.liquid      # Section 03: Swipeable combo bundle rail
│   │   ├── purelane-bundles.liquid     # Section 04: 3-tier pricing bundle cards
│   │   └── purelane-reviews.liquid     # Section 05: Auto-marquee customer review rail
│   └── snippets/
│       ├── purelane-product-card.liquid # Product card component (handles edge cases)
│       └── purelane-combo-card.liquid   # Combo card component (multi-item add to cart)
├── data/
│   └── seed-products.json         # 8 seed products (sold out, missing image, long title)
├── metafields/
│   └── schema-definitions.json    # Exportable Shopify metafield definitions
├── docs/
│   ├── purelane-homepage.html     # Original standalone design prototype
│   ├── build-notes.md             # Build notes (prototype fixes & architecture choices)
│   └── ai-workflow-notes.md       # AI workflow analysis (failure modes & scaling)
├── tests/                         # Automated test suite (Python unittest / pytest)
│   ├── test_phase0_spec.py
│   ├── test_phase1_hero.py
│   ├── test_phase2_shop_grid.py
│   ├── test_phase3_combos.py
│   ├── test_phase4_bundles.py
│   ├── test_phase5_reviews.py
│   └── test_phase6_integration.py
├── SPEC.md                        # Master source-of-truth technical specification
├── requirements.txt               # Dependencies for test environment
└── README.md                      # Project documentation
```

---

### **Key Features & Implementation Highlights**

1. **Pixel-Accurate Fidelity:**
   Matches prototype typography (`Outfit` & `Inter`), HSL tailored color palette (`:root` tokens), glassmorphism layers (`.glass`, `.glass-2`), depth scenes, and micro-animations from 375px up to 1440px+.

2. **Merchant Editable via Theme Editor:**
   All headings, copy, price displays, badge tags, collection selections, button URLs, and slideshow blocks are fully merchant-editable without touching code.

3. **Theme Editor Resilience (`shopify:section:load`):**
   JavaScript modules (`purelane-scripts.js`) listen to `shopify:section:load` events so slideshows, marquees, and reveal animations dynamically re-initialize without crashing when merchants add/remove/reorder sections in the Shopify Customizer.

4. **AJAX Multi-Item Cart Integration:**
   Combos and tier bundles issue multi-item `cart/add.js` POST requests and dispatch `cart:refresh` events to seamlessly update Dawn's slide-out drawer cart.

5. **Edge Case Guardrails:**
   - **Missing image:** Renders an inline SVG branded bottle placeholder.
   - **Sold out product:** Displays a disabled button styled cleanly within the theme palette.
   - **Long product titles:** Clamps title length to 2 lines via `-webkit-line-clamp: 2` without distorting grid heights.

6. **Accessibility & Core Web Vitals:**
   Includes visible focus rings, ARIA roles (`aria-label`, `aria-hidden`), and `prefers-reduced-motion` animation overrides.

---

### **Running Automated Tests**

Run the complete test suite locally across all section modules:

```powershell
python -m unittest discover tests
```

Or using `pytest`:

```powershell
pip install -r requirements.txt
pytest tests/ -v
```

---

### **Deliverables Summary**

- **Documentation & Specs:** [`SPEC.md`](SPEC.md), [`docs/build-notes.md`](docs/build-notes.md), [`docs/ai-workflow-notes.md`](docs/ai-workflow-notes.md)
- **Shopify Assets & Sections:** [`shopify/`](shopify/)
- **Seed Products & Metafields:** [`data/seed-products.json`](data/seed-products.json), [`metafields/schema-definitions.json`](metafields/schema-definitions.json)
