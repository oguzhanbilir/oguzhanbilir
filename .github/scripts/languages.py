"""Build generated/languages.svg from language bytes across all owned repos.
Only language totals are written; repo names never leave this script."""
import json, os, urllib.request
from html import escape

TOKEN = os.environ["STATS_TOKEN"]
API = "https://api.github.com"
SKIP = {"Jupyter Notebook"}  # notebook JSON inflates byte counts
COLORS = {"PHP": "#4F5D95", "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
          "HTML": "#e34c26", "CSS": "#663399", "Hack": "#878787", "Shell": "#89e051",
          "Batchfile": "#C1F12E", "Java": "#b07219", "C#": "#178600", "Vue": "#41b883",
          "SCSS": "#c6538c", "Dockerfile": "#384d54", "Blade": "#f7523f", "Kotlin": "#A97BFF"}

def get(url):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}",
                                               "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)

repos, page = [], 1
while True:
    batch = get(f"{API}/user/repos?affiliation=owner&visibility=all&per_page=100&page={page}")
    repos += batch
    if len(batch) < 100:
        break
    page += 1

totals, private = {}, 0
for r in repos:
    if r["fork"] or r["archived"]:
        continue
    private += r["private"]
    for lang, n in get(r["languages_url"]).items():
        if lang not in SKIP:
            totals[lang] = totals.get(lang, 0) + n
print(f"repos counted: {len(repos)} (private: {private})")
if private == 0:
    raise SystemExit("STATS_TOKEN sees no private repos; check its repository access")

total = sum(totals.values())
ranked = sorted(totals.items(), key=lambda x: -x[1])
top, rest = ranked[:8], sum(n for _, n in ranked[8:])
if rest:
    top.append(("Other", rest))
for k, v in top:
    print(f"{k}: {100 * v / total:.1f}%")

W, PAD, BAR_Y = 600, 20, 44
rows = (len(top) + 1) // 2
H = BAR_Y + 24 + rows * 26 + 8
parts, x = [], PAD
for k, v in top:
    w = (W - 2 * PAD) * v / total
    parts.append(f'<rect x="{x:.2f}" y="{BAR_Y}" width="{w:.2f}" height="10" fill="{COLORS.get(k, "#8b949e")}"/>')
    x += w
for i, (k, v) in enumerate(top):
    cx = PAD + (i % 2) * 290
    cy = BAR_Y + 40 + (i // 2) * 26
    parts.append(f'<circle cx="{cx + 6}" cy="{cy - 4}" r="6" fill="{COLORS.get(k, "#8b949e")}"/>'
                 f'<text x="{cx + 20}" y="{cy}" class="t">{escape(k)} '
                 f'<tspan class="m">{100 * v / total:.1f}%</tspan></text>')
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Languages across all repositories">
<style>.t{{font:500 14px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;fill:#8b949e}}.m{{fill:#8b949e;opacity:.75}}.h{{font:600 15px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;fill:#8b949e}}</style>
<text x="{PAD}" y="26" class="h">Languages across all my repos</text>
<clipPath id="c"><rect x="{PAD}" y="{BAR_Y}" width="{W - 2 * PAD}" height="10" rx="5"/></clipPath>
<g clip-path="url(#c)">{"".join(p for p in parts if p.startswith("<rect"))}</g>
{"".join(p for p in parts if p.startswith("<circle"))}
</svg>'''
os.makedirs("generated", exist_ok=True)
open("generated/languages.svg", "w").write(svg)
