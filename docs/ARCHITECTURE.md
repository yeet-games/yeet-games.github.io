# Architecture

Yeet Games is a static site. There is no server code and no build step.

## Components

| Part | Files | Job |
|---|---|---|
| Home page | `index.html`, `style.css`, `script.js` | Grid of games, search, category chips, a plain list of game page links |
| Catalog | `games.js` (`gamesData`, ~340 entries) | `id`, `name`, `categories`, `url`, `imgSrc` per game |
| Game loaders | `games/game.html`, `unity.html`, `Flash.html`, `Emulator.html`, `gameT.html` | Open a game in an iframe, Unity, Ruffle or an emulator |
| Game pages and bundles | `games/*.html`, `games/<name>/` | Vendored third-party games (HTML5, SWF, Unity data) |
| Other pages | `roblox.html`, `contact.html`, `Privacy-Policy.html`, `terms-of-service.html`, `404.html` | Site pages |
| Art | `cover/` (thumbnails), `img/`, `logo.png`, `fallback.png` | Images |
| SEO files | `sitemap.xml`, `robots.txt`, `scripts/generate-sitemap.py` | The script reads `games.js` and the page files, and writes the sitemap |
| Ads | `ads.txt`, tags in `index.html` | Ad network declarations and tags |

## Data flow

1. The browser loads `index.html`. `script.js` reads `gamesData` from `games.js` and builds the grid.
2. Search is client-side (debounced Levenshtein match). Category chips filter the same list.
3. A click opens the game `url`: a page in this repo, a loader with `?game=<url>`, or an external site.
4. Pages send pageviews to Plausible (`stats.senty.com.au`).
5. GitHub Pages serves the files from `master`. A push is the deploy.

## External services (no keys)

- Plausible, self-hosted: script from `stats.senty.com.au`, site `yeet-games.github.io`
- Ruffle from `unpkg.com`, Material Icons (Google Fonts), Font Awesome CDN
- Ad tags: `highperformanceformat.com` (Adsterra); `ads.txt` lists AdSense and partners
- Google Search Console via my-seo (property `https://yeet-games.github.io/`)
- Many games call their own external sites (for example diep.io, buildnow-gg.io)

## Environment variables

None. No secrets are used or stored.

## Hosting

GitHub Pages, org site `yeet-games.github.io`, source `master` `/`. No custom domain, no CNAME.
