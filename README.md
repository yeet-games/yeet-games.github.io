# Yeet Games (yeet-games.github.io)

> "The Best Place To Play over 100+ Games in school or at home." — site meta description

Yeet Games is an **unblocked games portal** served as a static site on GitHub Pages at
<https://yeet-games.github.io>. It hosts a searchable catalog of ~381 games (per `games.js`)
including HTML5 games, Flash games (played via Ruffle), Unity web builds, an emulator page,
and Roblox content, wrapped in a YouTube-style grid UI.

## Status

- **Active.** 9 commits on `master`; first commit `bc145a1` (2025-05-28, "first commit"),
  latest commit `61eba0e` (2026-05-27, "remove adsterra for now. too many complains").
- No CI/CD, no release process, no issue/PR templates.

## Stack

Pure static site — **no build system, no package manager, no framework**:

- HTML5 + CSS3 + vanilla JavaScript (`index.html`, `style.css`, `script.js`, `games.js`)
- Catalog data in `games.js` (`gamesData` array: `id`, `name`, `categories`, `url`, `imgSrc`)
- Client-side fuzzy search (Levenshtein distance) and category filtering in `script.js`
- [Ruffle](https://ruffle.rs) Flash emulator loaded from `unpkg.com/@ruffle-rs/ruffle` for `.swf` games
- [Plausible Analytics](https://stats.senty.com.au) (`data-domain="yeet-games.github.io"`, self-hosted instance)
- Material Icons (Google Fonts) and Font Awesome (CDN)
- Ad tags (Adsterra / highperformanceformat.com) inline in HTML + `ads.txt` (AdSense and partners)
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
games.js              Game catalog (gamesData array, ~381 entries)
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
- No `.github/workflows`, no `gh-pages` branch, no `CNAME` (site lives at
  `yeet-games.github.io`).
- **Deploy = push to `master`:**

```sh
git push origin master
```

## Maintenance notes

- `manifest.json` is stale: it still declares the old name `Sz-Games` and references
  `icons/manifest-icon-192.maskable.png` / `icons/manifest-icon-512.maskable.png`, which
  do not exist in the repo. **TODO:** rename to Yeet Games and add the icons.
- Leftover `Sz-Games` branding: `404.html` still reports analytics to
  `data-domain="sz-games.github.io"` and uses a `sz-games/home` favicon; `games/index.html`
  contains a link back to `https://sz-games.github.io`. The site appears to have been
  renamed from Sz-Games to Yeet Games. **TODO:** update or remove these references.
- `/GobalSettings.js` is referenced by `Privacy-Policy.html`, `games/Emulator.html`,
  `games/game.html`, `games/gameT.html`, and `games/unity.html` but **is not present in
  the repo** — those pages will request a 404. **TODO:** add the file or remove the tags.
- Ad state: the latest commit removed Adsterra snippets ("too many complains"), but
  `index.html` and `games/game.html` still include `highperformanceformat.com` ad tags.
  **TODO:** verify the intended ad configuration.
- Some catalog entries point to paths not present in the repo (e.g., `/home/webb/`,
  `/slope/`, `/Games9/bitlife`, `/storage3/AWeb/`) or to external sites. **TODO:** verify
  every catalog URL resolves.
- Repo size is ~310 MB (vendored game assets). Consider large-file hygiene (Git LFS) if it
  grows. **TODO** (if desired).
- No automated tests or CI. **TODO** (if desired): add a GitHub Actions smoke check.

## Credits & license

- Site maintained by Ruslan Osipov (`Rus <rusya13@gmail.com>` per git history).
- **No repository-level `LICENSE` file and no credits section exist in the site itself
  (Unknown).** Do not assume a license for the site code.
- Third-party game bundles are vendored under `games/` and retain their own licenses,
  e.g. `games/chess/license.txt` (GPL-3.0), `games/dino/LICENSE`,
  `games/Bin/.../hydra/scripts/pixi.min.js` (MIT). Respect each bundled game's license
  before redistributing.
