# Portfolio audit 2026-10 (FL-1108): row for yeet-games

Copy this row into `data/reports/portfolio-audit-2026-10.md` in the fleet repo. It was not edited there because that checkout belongs to other agents.

| project | stack | deps | vulns | backup | docs | proposal | PR |
|---|---|---|---|---|---|---|---|
| yeet-games | Static HTML/CSS/JS (~340 games, no build), GitHub Pages legacy build from master | n/a: no package manager; CDN Ruffle/Font Awesome unpinned | none in deps; Dependabot 0; no secrets found (grep, no gitleaks); secret scanning off | none needed: static, repo is the backup | README rewritten; ARCHITECTURE, CHANGELOG-TECH, PROPOSALS, AUDIT-2026-10 added; sitemap regenerated | no stack change; 9 small items (manifest, GobalSettings.js 404, sz-games leftovers, Adsterra decision) | branch task-2367 in yeet-games.github.io worktree (not pushed) |
