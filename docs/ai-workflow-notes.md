# AI Workflow & Agentic Engineering Notes

## Section 1: Tasks Delegated to AI Agents

1. **Prototype Spec Extraction:**
   Parsing design tokens, typography scales, color palettes, glassmorphism CSS rules, and component markup from monolithic HTML prototype (`docs/purelane-homepage.html`).

2. **Liquid Section & Schema Generation:**
   Generating Shopify section structures (`{% schema %}`, settings, blocks, presets) and converting static HTML components into Liquid syntax.

3. **Automated Test Suite Construction:**
   Writing unit and integration test modules (`tests/test_phase*.py`) to validate Liquid syntax, schema JSON compliance, accessibility hooks, and edge case handling.

---

## Section 2: Agent Failure Modes & Mitigations

1. **Schema JSON Syntax Validation Failures:**
   - *Failure:* AI agents occasionally inserted unescaped trailing commas or raw Liquid tags inside `{% schema %}` JSON blocks, breaking Shopify section parser.
   - *Mitigation:* Built strict regex schema extraction and `json.loads()` validation in phase test modules to catch invalid JSON instantly during build phase.

2. **Theme Editor Event Lifecycles:**
   - *Failure:* Standalone vanilla JS scripts initialized once on `DOMContentLoaded`, causing carousel animations and marquee observers to stop working when sections were dynamically reloaded in Shopify Theme Editor.
   - *Mitigation:* Enforced event wrapping around `shopify:section:load` custom events across all script modules.

3. **Multi-Item Cart Execution:**
   - *Failure:* Native Dawn theme default cart form only handled single item additions.
   - *Mitigation:* Architected multi-item JSON array payload handling on AJAX cart submit forms with fallback event dispatches.

---

## Section 3: Systematization Pipeline for 20+ Store Migrations

To scale this migration workflow across 20+ client sites per week:

1. **Automated Prototype AST Parser:**
   Build a Node/Python CLI tool that parses raw prototype HTML files and auto-generates Liquid sections, schema JSON, CSS token files, and seed product JSON.

2. **CI/CD Liquid Syntax & Schema Linter:**
   Establish GitHub Actions running `theme-check` and custom pytest validation suites on every pull request prior to pushing to live Shopify themes.

3. **Pre-Built Component Library:**
   Maintain a standardized library of Liquid snippets (`purelane-product-card`, `purelane-combo-card`, `purelane-drawer-cart`) with pluggable design token maps.
