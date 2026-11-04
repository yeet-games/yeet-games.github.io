# Yeet Games (yeet-games.github.io)

> "The Best Place To Play over 100+ Games in school or at home." — site meta description

Yeet Games is an **unblocked games portal** served as a static site on GitHub Pages at
<https://yeet-games.github.io>. It hosts a searchable catalog of ~340 games (per `games.js`)
including HTML5 games, Flash games (played via Ruffle), Unity web builds, an emulator page,
and Roblox content, wrapped in a YouTube-style grid UI.

## Status

- **Maintenance.** 21 commits on `master`; first commit `bc145a1` (2025-05-28), latest
  `87077fc` (2026-10-14, SEO work). Most recent work is SEO (sitemap, canonicals, game links).
- No CI/CD, no release process, no issue/PR templates. Audit: 2026-10-16, see
  `docs/AUDIT-2026-10.md`.

## Stack

Pure static site — **no build system, no package manager, no framework**:

- HTML5 + CSS3 + vanilla JavaScript (`index.html`, `style.css`, `script.js`, `games.js`)
- Catalog data in `games.js` (`gamesData` array: `id`, `name`, `categories`, `url`, `imgSrc`)
- Client-side fuzzy search (Levenshtein distance) and category filtering in `script.js`
- [Ruffle](https://ruffle.rs) Flash emulator loaded from `unpkg.com/@ruffle-rs/ruffle` for `.swf` games
- [Plausible Analytics](https://stats.senty.com.au) (`data-domain="yeet-games.github.io"`, self-hosted instance)
- Material Icons (Google Fonts) and Font Awesome (CDN)
- Ad tags (Adsterra / highperformanceformat.com) inline in `index.html` + `ads.txt` (AdSense and partners)
- `scripts/generate-sitemap.py` (Python 3, standard library only) builds `sitemap.xml`
- Web app manifest: `manifest.json`

## Prerequisites

- A web browser (any modern browser; the site targets desktop and mobile).
- For local serving only: any static file server (e.g., Python 3).
- No Node.js, no package installs, no API keys, no environment variables.

## Setup

```sh
git clone git@github.com:yeet-games/yeet-games.github.io.git
cd yeet-games.github.io
# no install step — the site is plain static files
```

## Local development

Serve the repo root over HTTP (iframes and absolute `/` paths work best over HTTP):

```sh
python3 -m http.server 8080
# open http://localhost:8080
```

Alternatively just open `index.html` directly in a browser (some absolute-path features
will be limited).

### Environment / configuration

There are **no environment variables or secrets**. External services are configured inline
in the HTML files (names only):

- Analytics: `data-domain` attribute + `stats.senty.com.au` script URL (`index.html`,
  `404.html`, `contact.html`, `games/*.html`, `roblox.html`)
- Ad network tags in `index.html` and `games/game.html`; network declarations in `ads.txt`
- CDN assets: Material Icons, Font Awesome, Ruffle

## Build / test

- **Sitemap:** after changing pages or `games.js`, run `python3 scripts/generate-sitemap.py`
  (`--check` fails if `sitemap.xml` is stale).
- **Build:** none. Commit and push; GitHub Pages serves the files as-is.
- **Test:** no automated test suite exists. Manual smoke checks:
  - `index.html` loads, search box filters the grid, category chips filter, thumbnails fall
    back to `fallback.png` on error
  - game links open in `games/game.html` (iframe via `?game=<url>`), `games/unity.html`
    (Unity), `games/Flash.html` (Ruffle/SWF)
  - secondary pages render: `contact.html`, `Privacy-Policy.html`, `terms-of-service.html`,
    `404.html`, `roblox.html`

## Architecture

```
index.html            Home: search, category chips, featured games, game grid
games.js              Game catalog (gamesData array, ~340 entries)
script.js             Renders grid; debounced Levenshtein search; category filter
style.css             Site styling
games/game.html       Generic game loader: fullscreen iframe (?game=<url>), loading screen
games/unity.html      Unity WebGL game loader
games/Flash.html      Flash (.swf) loader via Ruffle
games/Emulator.html   Emulator page
games/gameT.html      Legacy/alternate game template
roblox.html           Roblox page
contact.html          "Game Request" / "Report A Bug"
Privacy-Policy.html, terms-of-service.html, 404.html
cover/                Game thumbnails (425 images); fallback.png used on thumbnail errors
img/                  Additional artwork (e.g., buildnowgg.png, deepio.jpg)
games/                Vendored third-party game bundles (HTML5 builds, SWF files, Unity data)
manifest.json         Web app manifest
ads.txt               Ad network declarations
```

Game URLs in the catalog are either absolute (external sites such as `diep.io`,
`buildnow-gg.io`) or repo-relative paths served by GitHub Pages, opened through the
loader pages via the `?game=` query parameter.

## Deployment

- GitHub Pages **user/org site**: repo name `yeet-games.github.io` → Pages serves the
  root of the default branch (`master`).
- Pages source is branch `master`, path `/` (legacy build: the `pages build and deployment`
  run, last success 2026-10-15). No `.github/workflows`, no `gh-pages` branch, no `CNAME`.
- No server, no container, no Kamal. `hosts` is empty in the fleet `projects.toml`.
- **Deploy = push to `master`:**

```sh
git push origin master
```

## Connected services

- **Plausible** (self-hosted, `stats.senty.com.au`): site `yeet-games.github.io`. One page
  (`terms-of-service.html`) still reports `sz-games.github.io`.
- **my-seo / Google Search Console:** URL-prefix property `https://yeet-games.github.io/`
  (SEO and content history lives in my-seo annotations, not here).
- **Ads:** Adsterra tags in `index.html`, AdSense and partner lines in `ads.txt`. Revenue is in dash.
- No database, no R2/S3, no secrets, no other Senty services.

## Backups

Static site: **the Git repo is the backup** (GitHub `yeet-games/yeet-games.github.io`; ~220 MB
packed). No state on any server. Nothing to restore except a `git clone`.

## Docs

- `docs/ARCHITECTURE.md`: components, data flow, services
- `docs/CHANGELOG-TECH.md`: technical changes with dates
- `docs/PROPOSALS.md`: open fixes and upgrades
- `docs/AUDIT-2026-10.md`: the audit report (2026-10-16)

## Maintenance notes

Open problems are listed, with effort and risk, in `docs/PROPOSALS.md`. In short:
`manifest.json` still says `Sz-Games` and points to icons that do not exist; `/GobalSettings.js`
is requested but missing (404); `terms-of-service.html` and `404.html`/`games/index.html` carry
old Sz-Games references; Adsterra tags are still in `index.html` despite the May 2026 commit
that removed them; some catalog URLs may still be dead.

## Credits & license

- Owner: Rus (Ruslan Osipov, per git history). Fleet project `yeet-games`, todo prefix `YG`.
- **No repository-level `LICENSE` file and no credits section exist in the site itself
  (Unknown).** Do not assume a license for the site code.
- Third-party game bundles are vendored under `games/` and retain their own licenses,
  e.g. `games/chess/license.txt` (GPL-3.0), `games/dino/LICENSE`,
  `games/Bin/.../hydra/scripts/pixi.min.js` (MIT). Respect each bundled game's license
  before redistributing.
