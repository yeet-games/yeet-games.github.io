# Proposals

Open items from the 2026-10 audit. None is done in the audit PR.
Effort: S = under an hour, M = a few hours.

| # | What | Gain | Effort | Risk |
|---|---|---|---|---|
| 1 | Fix `manifest.json`: rename `Sz-Games` to `Yeet Games`, add the missing 192/512 icons (or drop the `icons` block) | Installable app works, no 404s | S | None |
| 2 | `GobalSettings.js` is requested by `games/game.html`, `unity.html`, `Emulator.html`, `gameT.html`, `Privacy-Policy.html` and is a 404. Remove the tags (or add the file) | No 404 on every game load | S | Low: check the games still run |
| 3 | `terms-of-service.html` reports to Plausible site `sz-games.github.io`. Change to `yeet-games.github.io`. Also `404.html` favicon and `games/index.html` "Back" link point to sz-games | Clean analytics, no traffic sent to the old brand | S | Low |
| 4 | Decide the ad setup. Commit 61eba0e said Adsterra was removed, but 3 `highperformanceformat.com` tags remain in `index.html` | Matches intent, fewer complaints | S | Revenue change (rus decides) |
| 5 | Dead catalog entry `https://yeet-games.github.io/home/webb/` (Infinite Tower) has no file in the repo. Fix or remove. Re-check external URLs | No dead cards | S | Low |
| 6 | Add a small GitHub Actions check: `python3 scripts/generate-sitemap.py --check` on PRs. Pin `actions/checkout@v7` | Stale sitemap caught | S | None |
| 7 | Repo is ~220 MB packed, 682 files (GitHub Pages limit is about 1 GB). Watch size; do not add big bundles. Git LFS does not work with Pages | Avoids hitting the limit | n/a | n/a |
| 8 | Add a licence/credits page for vendored games (chess GPL-3.0 etc.) | Licence compliance | M | Low |
| 9 | Vendored games and CDN scripts (Ruffle from unpkg `@latest`-style URL) are not pinned. Pin the Ruffle version | Stops silent breakage | S | Low |

## Stack

No stack change. A static site on GitHub Pages has no server cost, no memory use and no
runtime to maintain. There is no traffic or error evidence that a different stack would pay off.
