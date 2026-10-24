"""Build generated/languages.svg from language bytes across all owned repos.
Only language totals are written; repo names never leave this script."""
import json, os, sys, urllib.request
from html import escape

API = "https://api.github.com"
ALIAS = {"Hack": "PHP"}  # linguist tags some .php files as Hack
SKIP = {"Jupyter Notebook"}  # notebook JSON inflates byte counts
COLORS = {  # GitHub linguist colors
    "PHP": "#4F5D95", "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "HTML": "#e34c26", "CSS": "#663399", "Hack": "#878787", "Shell": "#89e051",
    "Batchfile": "#C1F12E", "Java": "#b07219", "C#": "#178600", "Vue": "#41b883",
    "SCSS": "#c6538c", "Dockerfile": "#384d54", "Blade": "#f7523f", "Kotlin": "#A97BFF",
    "Dart": "#00B4AB", "C++": "#f34b7d", "C": "#555555", "Go": "#00ADD8", "Twig": "#c1d026",
    "PowerShell": "#012456", "Less": "#1d365d", "Other": "#6e7681",
}


def collect():
    token = os.environ.get("STATS_TOKEN", "").strip()
    if not token:
        sys.exit("STATS_TOKEN is empty: add it under Settings > Secrets and variables > Actions > Repository secrets")

    def get(url):
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}",
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
                lang = ALIAS.get(lang, lang)
                totals[lang] = totals.get(lang, 0) + n
    print(f"repos counted: {len(repos)} (private: {private})")
    if private == 0:
        sys.exit("STATS_TOKEN sees no private repos; give it access to all repositories")
    return totals


def render(totals):
    total = sum(totals.values())
    ranked = sorted(totals.items(), key=lambda x: -x[1])
    top = ranked[:8]
    rest = sum(n for _, n in ranked[8:])
    if rest and round(100 * rest / total, 1) > 0:
        top.append(("Other", rest))
    items = [(k, 100 * v / total) for k, v in top if round(100 * v / total, 1) > 0]
    for k, p in items:
        print(f"{k}: {p:.1f}%")

    W, P = 480, 25
    bar_y, bar_h, gap = 62, 10, 2
    rows = (len(items) + 1) // 2
    H = bar_y + bar_h + 28 + rows * 26 + 14
    font = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
    inner = W - 2 * P
    usable = inner - gap * (len(items) - 1)
    segs, x = [], P
    for k, p in items:
        w = max(usable * p / 100, 2)
        segs.append(f'<rect x="{x:.2f}" y="{bar_y}" width="{w:.2f}" height="{bar_h}" fill="{COLORS.get(k, "#6e7681")}"/>')
        x += w + gap
    legend = []
    for i, (k, p) in enumerate(items):
        cx = P + (i % 2) * (inner / 2)
        cy = bar_y + bar_h + 34 + (i // 2) * 26
        legend.append(
            f'<circle cx="{cx + 5:.1f}" cy="{cy - 4.5}" r="5" fill="{COLORS.get(k, "#6e7681")}"/>'
            f'<text x="{cx + 18:.1f}" y="{cy}" class="l">{escape(k)}</text>'
            f'<text x="{cx + inner / 2 - 16:.1f}" y="{cy}" class="p" text-anchor="end">{p:.1f}%</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Most used languages">
<style>
.t{{font:600 18px {font};fill:#e6edf3}}
.l{{font:400 13px {font};fill:#c9d1d9}}
.p{{font:400 13px {font};fill:#8b949e}}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
<text x="{P}" y="38" class="t">Most used languages</text>
<clipPath id="bar"><rect x="{P}" y="{bar_y}" width="{inner}" height="{bar_h}" rx="5"/></clipPath>
<g clip-path="url(#bar)">{"".join(segs)}</g>
{"".join(legend)}
</svg>
'''


if __name__ == "__main__":
    data = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else collect()
    os.makedirs("generated", exist_ok=True)
    with open("generated/languages.svg", "w") as f:
        f.write(render(data))
