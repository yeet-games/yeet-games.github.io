# FL-1453: sitemap check (idea 1)

Checked 2026-10-24.

- `xmllint --noout sitemap.xml`: valid XML.
- Live `https://yeet-games.github.io/sitemap.xml`: HTTP 200, `content-type: application/xml`.
- `robots.txt` allows all and names the sitemap.
- All 19 URLs in the sitemap return HTTP 200.

No site change is needed. The remaining steps need Google Search Console (see the PR body).
