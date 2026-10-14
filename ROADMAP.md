# Roadmap — brand.paruto.com

The single list of what has been built, what is in progress and what is left for the Paruto brand guide. Every feature has a permanent ID so it can be referenced in commits, chats and issues.

**Live tracker:** https://claude.ai/artifact/QzSYH6BDttCECDSCKAxJ1W — the same items with status changes, history and filters. Keep both in step: when an item changes in one, update the other.

**Last updated:** 2026-10-14 · **Live version:** v1.0 · **Site:** https://brand.paruto.com

## How to use this file

**Statuses**

| Status | Meaning |
| --- | --- |
| ✅ Shipped | Live on brand.paruto.com. Has a ship date and commit. |
| 🚧 In progress | Being built now. |
| 📋 Planned | Agreed and scheduled; next in line. |
| 💡 Proposed | A suggestion that hasn't been agreed yet. Promote it to Planned or drop it. |
| ❓ Needs decision | Blocked until Jonathan decides or confirms something. |
| 🗑️ Dropped | Decided against. Kept for the record with a reason. |

**Priority:** P1 = do next · P2 = soon · P3 = later.

**Rules for keeping it current**
1. **New idea or request:** add a row at the bottom of the right section with the next free ID (next free: **BG-068**), status 💡 Proposed (or 📋 Planned if already agreed) and today's date in *Added*.
2. **Starting work:** set 🚧 In progress.
3. **Shipped:** move the row to *Shipped*, set the ship date and the commit hash, and reference the ID in the commit message (e.g. `BG-030: raise muted text contrast`).
4. **Never reuse or renumber IDs.** Dropped items stay, marked 🗑️ with a reason.
5. Update **Last updated** and the counts in *At a glance* whenever this file changes.

## At a glance

| ✅ Shipped | 🚧 In progress | 📋 Planned | 💡 Proposed | ❓ Needs decision |
| --- | --- | --- | --- | --- |
| 11 | 0 | 6 | 19 | 4 |

---

## ✅ Shipped

| ID | Feature | Shipped | Commit |
| --- | --- | --- | --- |
| BG-001 | Brand guide site: cover, index and 13 sections (overview, logo story, architecture, logo system, symbol variants, colour, typography, clear space, usage table, brand in use, icons, do's & don'ts, downloads) | 2026-10-08 | `17cc4c3` |
| BG-002 | P/D symbol redrawn as vector geometry; all lettering outlined from Montserrat; one generator script (`scripts/build_logos.py`) | 2026-10-08 | `17cc4c3` |
| BG-003 | Master logo set: horizontal, stacked and symbol in gold, black and white (SVG + PNG) | 2026-10-08 | `17cc4c3` |
| BG-004 | Company lockups for Paruto Media (with "We Amplify Impact"), Music and Capital | 2026-10-08 | `17cc4c3` |
| BG-005 | Favicon, Apple touch icon, PWA icons (192/512), web manifest and 1200×630 social share image | 2026-10-08 | `17cc4c3` |
| BG-006 | Downloads section with per-file SVG/PNG links and a complete asset ZIP | 2026-10-08 | `17cc4c3` |
| BG-007 | Brand-in-use mockups: business card, letterhead, social (banner, post, avatar, story), email signature, website | 2026-10-08 | `17cc4c3` |
| BG-008 | Interactions: click-to-copy colour swatches, scroll progress, mobile menu, active-section highlighting, reveal on scroll, reduced-motion support | 2026-10-08 | `17cc4c3` |
| BG-009 | Deployed on GitHub Pages at brand.paruto.com with enforced HTTPS | 2026-10-08 | `1ed144c` |
| BG-010 | Title changed to Founder on the business card and email signature | 2026-10-08 | `4af43fa`, `cb717e8` |
| BG-011 | Paruto Kids lockup, added across overview, architecture, website mockup, footer and downloads | 2026-10-10 | `7176113` |

## 🚧 In progress

_Nothing in progress._

## ❓ Needs decision

| ID | Item | Added | What's needed |
| --- | --- | --- | --- |
| BG-020 | Confirm drafted copy | 2026-10-14 | Purpose, Positioning and Voice lines; the "Think Possibilities" statement; the logo story extended to the group; the Music and Capital descriptions. All were drafted, none confirmed. |
| BG-021 | Confirm contact details in mockups | 2026-10-14 | Phone +234 817 017 9552 and the Katampe, Kado address on the card, letterhead and signature came from the Media guide. Confirm they're right for the group. |
| BG-022 | Light theme or dark-only? | 2026-10-14 | Your standard is Light / Dark / System in every app; the guide is dark-only to match brand.parutomedia.com. Decide which wins. If light, a light theme gets added as a new feature. |
| BG-023 | Run the launch checklist | 2026-10-14 | The site went live before your launch-checklist rule. Run it now and decide on any FAIL items. |

## 📋 Planned — accessibility & HIG basics (P1)

These close gaps against your standing HIG/accessibility rules. Measured on 2026-10-14.

| ID | Feature | Priority | Added | Notes |
| --- | --- | --- | --- | --- |
| BG-030 | Raise text contrast to 4.5:1 or better | P1 | 2026-10-14 | Muted text measures 4.0–4.1:1, desktop nav links 3.0:1, faint labels 1.6:1. Gold on black (7.5:1) is fine. |
| BG-031 | Tap targets of at least 44×44 pt | P1 | 2026-10-14 | SVG/PNG download capsules are about 26 px tall; footer and file-list links are similar. |
| BG-032 | Text that scales with the user's text-size setting | P1 | 2026-10-14 | 71 font sizes are fixed in px; move to rem. |
| BG-033 | Honour Reduce Transparency | P1 | 2026-10-14 | Nav and mobile menu use backdrop blur; add a solid fallback under `prefers-reduced-transparency`. |
| BG-034 | Keyboard and screen-reader pass | P1 | 2026-10-14 | Skip link, focus trapped in the open mobile menu, visible focus everywhere, check every image's alt text. |
| BG-035 | Safe-area-aware layout | P1 | 2026-10-14 | `viewport-fit=cover` is set but nothing uses `env(safe-area-inset-*)`; back-to-top button and nav can sit under the notch or home indicator. |

## 💡 Proposed — match the Paruto Media guide (P2)

Sections the Media guide has that this guide doesn't yet.

| ID | Feature | Priority | Added | Notes |
| --- | --- | --- | --- | --- |
| BG-040 | Presentation slides: mockups plus a downloadable deck template | P2 | 2026-10-14 | |
| BG-041 | Video end card and watermark guidance, with assets | P2 | 2026-10-14 | Media guide: white symbol, 55–65% opacity, bottom-right; end card held 5–8 s. |
| BG-042 | Outdoor and large format: billboard, pull-up banner, ID badge | P2 | 2026-10-14 | |
| BG-043 | Merchandise mockups | P2 | 2026-10-14 | |
| BG-044 | Proposal / document cover mockup | P2 | 2026-10-14 | Gold on black cover, black on white interior. |

## 💡 Proposed — templates & production files (P2)

| ID | Feature | Priority | Added | Notes |
| --- | --- | --- | --- | --- |
| BG-050 | Email signature generator: fill in name and role, copy HTML | P2 | 2026-10-14 | Lets every staff member produce a correct signature. |
| BG-051 | Print-ready business card files (PDF with bleed and crop marks) | P2 | 2026-10-14 | |
| BG-052 | Letterhead template (Word and Google Docs) | P2 | 2026-10-14 | |
| BG-053 | Social media templates at every platform size | P2 | 2026-10-14 | Profile, post, story, LinkedIn/X/Facebook/YouTube banners. |
| BG-054 | Flat-gold logo files for foil, embroidery and single-colour print, with print colour references | P2 | 2026-10-14 | Current gold files use a gradient. Print colour equivalents need to be confirmed with a printer. |
| BG-055 | Company lockups for future Paruto companies | P2 | 2026-10-14 | One line in `build_logos.py` per company; add as each one launches. |

## 💡 Proposed — content (P3)

| ID | Feature | Priority | Added | Notes |
| --- | --- | --- | --- | --- |
| BG-060 | Voice & messaging: tone, words to use and avoid, company boilerplate | P3 | 2026-10-14 | Needs your input; don't invent. |
| BG-061 | Photography and imagery guidelines | P3 | 2026-10-14 | Needs real Paruto photography. |
| BG-062 | Changelog / version history section in the guide | P3 | 2026-10-14 | Shows what changed between guide versions (v1.0 → v1.1). |
| BG-063 | Printable PDF of the whole guide | P3 | 2026-10-14 | For partners who need an attachment. |

## 💡 Proposed — site & experience (P3)

| ID | Feature | Priority | Added | Notes |
| --- | --- | --- | --- | --- |
| BG-064 | Premium hero: the P/D symbol rendered in three.js (WebGL) or Rive | P3 | 2026-10-14 | Your standard for public landing pages. Load after first paint, static fallback, respect Reduce Motion, no Lighthouse regression. |
| BG-065 | robots.txt, sitemap.xml and a branded 404 page | P3 | 2026-10-14 | None exist yet. |
| BG-066 | Privacy-friendly analytics (visits and asset downloads) | P3 | 2026-10-14 | Needs a decision on tool; no cookies preferred. |
| BG-067 | Link to the guide from paruto.com | P3 | 2026-10-14 | Live paruto.com has no link yet; the redesign in `~/Projects/paruto-com` already links to it. Ships when that redesign deploys. |

## 🗑️ Dropped

_Nothing dropped._
