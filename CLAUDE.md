# Paruto brand guide (brand.paruto.com)

Static, single-page brand guide. See README.md for layout, preview and deploy.

- **Never hand-edit files in `assets/logos/`, `assets/icons/` or the zip.** Change `scripts/build_logos.py` and rerun it (`.venv/bin/python scripts/build_logos.py`; create the venv per README if missing). The script also rebuilds `paruto-brand-assets.zip`.
- Design tokens live at the top of `styles.css` (gold `#C9952A`, black `#0A0A0A`, Barlow / Barlow Condensed / Cormorant Garamond). The site is dark-only by design, matching brand.parutomedia.com.
- Brand facts: master tagline "Think Possibilities"; subsidiaries Paruto Media (parutomedia.com, tagline "We Amplify Impact", its own guide at brand.parutomedia.com), Paruto Music (parutomusic.com), Paruto Capital (parutocapital.com), Paruto Kids (parutokids.com; songs, stories and play for ages 2–5; standard lockup, no tagline); contact hello@paruto.com. Don't invent new facts, stats or taglines — ask.
- Deploy: GitHub Pages; every push to `main` redeploys. Don't push without being asked.
- **Roadmap:** `ROADMAP.md` is the source of truth for what's built and what's left. When a feature is requested, started, shipped or dropped, update it in the same change (follow the rules at the top of that file) and put the feature ID in the commit message. The same items live in the tracker artifact https://claude.ai/artifact/QzSYH6BDttCECDSCKAxJ1W (collection `items`, one document per ID, each with a `history` list); update that row with the ArtifactData tool too, appending a history entry with `by: "claude"`.
