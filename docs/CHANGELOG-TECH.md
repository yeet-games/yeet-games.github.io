# Technical changelog

Technical changes only. SEO and content changes are in the my-seo annotations for
`https://yeet-games.github.io/`.

| Date | Commit | Change |
|---|---|---|
| 2025-05-28 | bc145a1 | First commit: static portal on GitHub Pages (`master`), forked from the Sz-Games site |
| 2026-05-19 | 8c8a27b, 53fea82 | Ad tags added |
| 2026-05-27 | 61eba0e | Adsterra snippets partly removed ("too many complains"); some tags remain in `index.html` |
| 2026-08-13 | 18606d8 | README added |
| 2026-10-04 | 6c79c41 | `robots.txt` and a first `sitemap.xml` |
| 2026-10-04 | 21755de, d3122ce | Self-canonical on every page; none on `404.html` |
| 2026-10-05 | 67c90b9 | `scripts/generate-sitemap.py` builds `sitemap.xml` from `games.js` |
| 2026-10-08 | 05960f6 | 40 dead catalog links dropped (381 → 341 entries), Backrooms path fixed |
| 2026-10-14 | 87077fc | PR #2: plain-HTML list of game page links, catalog links point at sitemap URLs, canonical on 14 game pages |
| 2026-10-16 | (audit) | Docs added (sitemap left as on master) |

No framework, deploy pipeline or server changes ever: it has been GitHub Pages from `master` throughout.
