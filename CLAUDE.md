# Paruto brand guide (brand.paruto.com)

Static, single-page brand guide. See README.md for layout, preview and deploy.

- **Never hand-edit files in `assets/logos/`, `assets/icons/` or the zip.** Change `scripts/build_logos.py` and rerun it (`.venv/bin/python scripts/build_logos.py`; create the venv per README if missing). The script also rebuilds `paruto-brand-assets.zip`.
- Design tokens live at the top of `styles.css` (gold `#C9952A`, black `#0A0A0A`, Barlow / Barlow Condensed / Cormorant Garamond). The site is dark-only by design, matching brand.parutomedia.com.
- Brand facts: master tagline "Think Possibilities"; subsidiaries Paruto Media (parutomedia.com, tagline "We Amplify Impact", its own guide at brand.parutomedia.com), Paruto Music (parutomusic.com), Paruto Capital (parutocapital.com); contact hello@paruto.com. Don't invent new facts, stats or taglines — ask.
- Deploy: GitHub Pages; every push to `main` redeploys. Don't push without being asked.
