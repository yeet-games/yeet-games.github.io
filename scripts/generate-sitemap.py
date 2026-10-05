#!/usr/bin/env python3
"""Generate sitemap.xml for yeet-games.github.io.

The sitemap lists the static pages and every game page that the catalog
(games.js) links and that this repository serves. lastmod is the date of
the last commit that touched the page file. A file with uncommitted
changes uses today.

Usage:

    python3 scripts/generate-sitemap.py          # write sitemap.xml
    python3 scripts/generate-sitemap.py --check  # fail if sitemap.xml is stale
"""

import datetime
import os
import re
import subprocess
import sys
import urllib.parse
from xml.sax.saxutils import escape

BASE = 'https://yeet-games.github.io'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, 'sitemap.xml')

# Static pages, in sitemap order. (url, page file, priority)
SITE_PAGES = [
    ('/', 'index.html', '1.00'),
    ('/roblox.html', 'roblox.html', '0.80'),
]
LEGAL_PAGES = [
    ('/contact.html', 'contact.html', '0.40'),
    ('/Privacy-Policy.html', 'Privacy-Policy.html', '0.40'),
    ('/terms-of-service.html', 'terms-of-service.html', '0.40'),
]
GAME_PRIORITY = '0.80'

# Loader pages open a game from the ?game= parameter. The game page in the
# parameter is the one to list, never the loader page itself.
LOADER_PAGES = {
    'games/game.html',
    'games/unity.html',
    'games/Flash.html',
    'games/Emulator.html',
    'games/gameT.html',
}


def catalog_urls():
    """Return every url value in games.js, in file order."""
    with open(os.path.join(ROOT, 'games.js'), encoding='utf-8') as fh:
        source = fh.read()
    single = re.findall(r"url:\s*'([^']*)'", source)
    double = re.findall(r'url:\s*"([^"]*)"', source)
    return single + double


def local_path(url):
    """Return the URL path on this site, or None for another site."""
    if url.startswith(BASE):
        return url[len(BASE):]
    if url.startswith('//') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url):
        return None
    if url.startswith('./'):
        return url[1:]
    if url.startswith('/'):
        return url
    return '/' + url


def page_file(url):
    """Return the repo file that serves a catalog URL, or None if none does."""
    path = local_path(url)
    if path is None:
        return None
    parsed = urllib.parse.urlsplit(path)
    request = urllib.parse.unquote(parsed.path).strip('/')
    if request in LOADER_PAGES:
        target = urllib.parse.parse_qs(parsed.query).get('game', [None])[0]
        return page_file(target) if target else None
    if not request:
        return 'index.html'
    candidates = []
    if request.endswith('/'):
        candidates.append(request + 'index.html')
    else:
        candidates.append(request + '/index.html')
        candidates.append(request + '.html')
        candidates.append(request)
    for candidate in candidates:
        if candidate in LOADER_PAGES or not candidate.endswith('.html'):
            continue
        if os.path.isfile(os.path.join(ROOT, candidate)):
            return candidate
    return None


def page_url(rel):
    """Return the canonical site URL for a repo page file."""
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[: -len('index.html')]
    return '/' + rel


def game_pages():
    """Return (url, file) for every game page the catalog links, sorted."""
    pages = {}
    for url in catalog_urls():
        rel = page_file(url)
        if rel:
            pages[page_url(rel)] = rel
    return sorted(pages.items(), key=lambda pair: pair[0].lower())


def lastmod(rel):
    """Return the last change date of a repo file as YYYY-MM-DD."""
    dirty = subprocess.run(
        ['git', 'status', '--porcelain', '--', rel],
        cwd=ROOT, capture_output=True, text=True,
    )
    if dirty.returncode == 0 and dirty.stdout.strip():
        return datetime.date.today().isoformat()
    log = subprocess.run(
        ['git', 'log', '-1', '--format=%cs', '--', rel],
        cwd=ROOT, capture_output=True, text=True,
    )
    if log.returncode == 0 and re.fullmatch(r'\d{4}-\d{2}-\d{2}', log.stdout.strip()):
        return log.stdout.strip()
    return datetime.date.fromtimestamp(
        os.path.getmtime(os.path.join(ROOT, rel))
    ).isoformat()


def render():
    """Return the full sitemap.xml text."""
    pages = game_pages()
    if not pages:
        sys.exit('error: no game pages found; did the games.js format change?')
    static_urls = {url for url, _, _ in SITE_PAGES + LEGAL_PAGES}
    games = [(url, rel) for url, rel in pages if url not in static_urls]
    entries = list(SITE_PAGES)
    entries += [(url, rel, GAME_PRIORITY) for url, rel in games]
    entries += LEGAL_PAGES
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    assert len({url for url, _, _ in entries}) == len(entries), 'duplicate URL'
    for url, rel, priority in entries:
        lines += [
            '  <url>',
            '    <loc>%s</loc>' % escape(BASE + url),
            '    <lastmod>%s</lastmod>' % lastmod(rel),
            '    <priority>%s</priority>' % priority,
            '  </url>',
        ]
    lines.append('</urlset>')
    return '\n'.join(lines) + '\n'


def main():
    generated = render()
    if '--check' in sys.argv[1:]:
        current = ''
        if os.path.exists(SITEMAP):
            with open(SITEMAP, encoding='utf-8') as fh:
                current = fh.read()
        if current != generated:
            sys.exit('sitemap.xml is stale; run scripts/generate-sitemap.py')
        print('sitemap.xml is current (%d URLs)' % generated.count('<loc>'))
        return 0
    with open(SITEMAP, 'w', encoding='utf-8') as fh:
        fh.write(generated)
    print('wrote sitemap.xml (%d URLs)' % generated.count('<loc>'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
