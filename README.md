# Paruto Brand Guide — brand.paruto.com

The official brand identity guide for Paruto and its companies (Paruto Media, Paruto Music, Paruto Capital, Paruto Kids). Static site, no build step for the page itself.

```
index.html, styles.css, app.js   the guide
assets/logos/                    every logo, symbol and company lockup (SVG + PNG)
assets/icons/                    favicons, app icons, social share image
paruto-brand-assets.zip          the downloadable pack (generated)
scripts/build_logos.py           generates all of the above from one source
scripts/fonts/                   Montserrat (OFL) used for the logotype outlines
```

## Preview locally
```bash
python3 -m http.server 8090   # open http://localhost:8090
```

## Regenerating logos
All artwork comes from `scripts/build_logos.py`: the P/D symbol is drawn as vector geometry and all lettering is converted to outlines, so files never depend on installed fonts. To add a new company lockup, add it to `SUBSIDIARIES` and rerun:
```bash
python3 -m venv .venv && .venv/bin/pip install fonttools resvg-py
.venv/bin/python scripts/build_logos.py
```
Then add the new lockup to the Brand Architecture section in `index.html` and the download list in `app.js`.

## Deploying
GitHub Pages from `main` (`CNAME` + `.nojekyll` at the root — don't delete them). DNS: a CNAME record `brand` → `jonathanobise.github.io.`
