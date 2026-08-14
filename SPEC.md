# Spec Document: Purelane → Shopify Dawn Sections

Master source of truth for converting `docs/purelane-homepage.html` prototype into merchant-editable Shopify Liquid sections.

---

## 1. Design Tokens (from prototype `:root`)

```css
:root {
  --ink: #17102b;
  --deep: #241a3d;
  --brand: #4b3a8f;
  --brand-lt: #6b55b8;
  --paper: #ece6f7;
  --paper-2: rgba(236, 230, 247, 0.74);
  --paper-3: rgba(236, 230, 247, 0.52);
  --accent: #f0a03c;
  --accent-2: #c9761d;
  --surface: #faf7fd;
  --g-bg: linear-gradient(158deg, rgba(236, 230, 247, 0.15), rgba(75, 58, 143, 0.20) 58%, rgba(23, 16, 43, 0.28));
  --g-line: rgba(236, 230, 247, 0.22);
  --g-shadow: 0 26px 74px rgba(18, 12, 34, 0.44);
  --g-inset: inset 0 1px 0 rgba(255, 255, 255, 0.24);
  --r: 26px;
  --r-sm: 16px;
  --maxw: 1180px;
  --sec-y: 34px;
  --ease: cubic-bezier(0.2, 0.7, 0.2, 1);
}
```
**Typography:**
- Display/Headings: `Outfit`, system-ui, sans-serif (Weights: 500, 600, 700, 800)
- Body: `Inter`, system-ui, sans-serif (Weights: 400, 500, 600, 700)

---

## 2. Section Inventory

| # | Liquid File | Section Anchor | Renders |
|---|---|---|---|
| 01 | `shopify/sections/purelane-hero.liquid` | `section.hero` | Fullscreen hero, bottle stage switcher (1→2→3 products), badge strip, 2 CTA buttons |
| 02 | `shopify/sections/purelane-shop-grid.liquid` | `#shop` | Product grid with collection binding. Pill badge, rating, price/compare, AJAX add-to-cart |
| 03 | `shopify/sections/purelane-combos.liquid` | `#combos` | Horizontal swipeable combo rail: 5 preset cards, product image stacks, savings badge |
| 04 | `shopify/sections/purelane-bundles.liquid` | `#bundles` | 3-tier pricing (2/3/5 products). Bundle AJAX add-to-cart |
| 05 | `shopify/sections/purelane-reviews.liquid` | `#reviews` | Auto-marquee review rail, aggregate star header |

---

## 3. Glassmorphism Design Contract

```css
.glass {
  background: var(--g-bg);
  backdrop-filter: blur(24px) saturate(150%);
  -webkit-backdrop-filter: blur(24px) saturate(150%);
  border: 1px solid var(--g-line);
  border-radius: var(--r);
  box-shadow: var(--g-shadow), var(--g-inset);
  position: relative;
  overflow: hidden;
}

.glass-2 {
  background: linear-gradient(158deg, rgba(236, 230, 247, 0.10), rgba(0, 48, 46, 0.22));
  backdrop-filter: blur(18px) saturate(135%);
  -webkit-backdrop-filter: blur(18px) saturate(135%);
  border: 1px solid rgba(236, 230, 247, 0.16);
  border-radius: var(--r);
  box-shadow: 0 18px 48px rgba(18, 12, 34, 0.36), inset 0 1px 0 rgba(255, 255, 255, 0.16);
  position: relative;
  overflow: hidden;
}
```

---

## 4. Reveal & Stagger Animation Contract

- Initial state `.rv`: `opacity: 0; transform: translateY(30px); filter: blur(7px)`
- Active state `.rv.in`: `opacity: 1; transform: none; filter: none`
- Stagger Delays:
  - `.rv-d1`: 90ms
  - `.rv-d2`: 180ms
  - `.rv-d3`: 270ms
  - `.rv-d4`: 360ms
  - `.rv-d5`: 450ms
- Intersection Observer triggers `.in` when `entry.isIntersecting` is true (`rootMargin: "0px 0px -12% 0px"`).
- `@media (prefers-reduced-motion: reduce)` overrides to instant display (`opacity: 1; transform: none; filter: none`).
- Re-initialized on `shopify:section:load` event.

---

## 5. AJAX Cart Payload Specs

Multi-item POST payload for combos and bundles:
```json
{
  "items": [
    { "id": 123456789, "quantity": 1, "properties": { "_bundle": "Kitchen Essentials" } },
    { "id": 987654321, "quantity": 1, "properties": { "_bundle": "Kitchen Essentials" } }
  ]
}
```
Triggers `document.dispatchEvent(new CustomEvent('cart:refresh'))` after successful POST to `/cart/add.js`.

---

## 6. Metafield Definitions

| Namespace.Key | Type | Purpose |
|---|---|---|
| `custom.rating_score` | `number_decimal` | Rating out of 5 (e.g. 4.9) |
| `custom.review_count` | `number_integer` | Number of reviews (e.g. 1420) |
| `custom.badge_text` | `single_line_text_field` | Product card pill badge (e.g. "Bestseller") |
| `custom.benefit_tag` | `single_line_text_field` | Tagline for combo card products |
| `custom.combo_products` | `list.product_reference` | Products in combo bundle |

---

## 7. Edge Cases Contract

1. **Missing Product Image:** Fallback SVG gradient bottle container rendered.
2. **Sold Out Product:** Button disabled with text "Sold Out", visual opacity remains readable.
3. **Long Product Title:** Line-clamp CSS (`-webkit-line-clamp: 2`) limits title to 2 lines max with ellipsis without breaking grid heights.
