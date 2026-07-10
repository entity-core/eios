#!/usr/bin/env python3
"""Render the canonical EIOS spec markdown into the branded HTML document.

Usage: python3 tools/render_html.py
Reads  spec/eios-1.0-master-documentation.md
Writes spec/eios-1.0-master-documentation.html

Dependency-free: parses the constrained markdown subset used by the spec
(h1-h4, paragraphs, lists, tables, fenced code, single-paragraph
blockquotes, hr, inline bold/italic/code/links).
"""
import html as html_mod
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "spec" / "eios-1.0-master-documentation.md"
DST = ROOT / "spec" / "eios-1.0-master-documentation.html"

NAV_GROUPS = [
    ("Overview", 1, 4),
    ("Entity Foundation", 5, 12),
    ("Actors and Boundaries", 13, 15),
    ("Information Model", 16, 20),
    ("Weave and Views", 21, 22),
    ("Governance and Operations", 23, 29),
    ("Lifecycle and Use", 30, 33),
    ("Implementation and Continuity", 34, 36),
    ("Reference", 37, 39),
]


def gh_slug(text):
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def inline(text):
    # protect code spans
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes)-1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html_mod.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<em>\1</em>", text)
    text = re.sub(
        r"\x00(\d+)\x00",
        lambda m: "<code>" + html_mod.escape(codes[int(m.group(1))]) + "</code>",
        text,
    )
    return text


def render_table(rows):
    header = rows[0]
    body = rows[2:]
    out = ["<table>", "<thead><tr>"]
    for cell in header:
        out.append(f"<th>{inline(cell)}</th>")
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def blocks_to_html(lines):
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            lang = line[3:].strip()
            buf = []
            i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = html_mod.escape("\n".join(buf))
            if lang:
                out.append(f"<pre><code>{code}</code></pre>")
            else:
                out.append(f'<div class="diagram">{code}</div>')
            continue
        if line.startswith("#### "):
            out.append(f"<h4>{inline(line[5:])}</h4>")
            i += 1
            continue
        if line.startswith("### "):
            title = line[4:]
            out.append(f'<h3 id="{gh_slug(title)}">{inline(title)}</h3>')
            i += 1
            continue
        if line.startswith("> "):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip())
                i += 1
            out.append(f'<div class="callout">{inline(" ".join(buf))}</div>')
            continue
        if line.strip() == "---":
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            out.append(render_table(rows))
            continue
        if re.match(r"^- ", line):
            out.append("<ul>")
            while i < n and re.match(r"^- ", lines[i]):
                out.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("</ul>")
            continue
        if re.match(r"^\d+\. ", line):
            out.append("<ol>")
            while i < n and re.match(r"^\d+\. ", lines[i]):
                out.append(f"<li>{inline(re.sub(r'^\\d+\\. ', '', lines[i]))}</li>")
                i += 1
            out.append("</ol>")
            continue
        # paragraph: consume until blank line or block start
        buf = []
        while i < n and lines[i].strip() and not re.match(
            r"^(#{1,4} |> |```|\||- |\d+\. |---$)", lines[i]
        ):
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


def main():
    text = SRC.read_text()
    lines = text.split("\n")

    # header: h1, subtitle paragraph, pills line
    assert lines[0].startswith("# ")
    h1 = lines[0][2:]
    subtitle = lines[2]
    pills_line = lines[4]
    pills = re.findall(r"`([^`]+)`", pills_line)
    pills += ["Canonical: github.com/entity-core/eios"]

    # body starts after the Contents block: find second '---' after pills
    hr_idx = [i for i, l in enumerate(lines) if l.strip() == "---"]
    body_start = hr_idx[1] + 1

    # split into h2 sections
    sections = []  # (num, title, lines)
    cur = None
    for line in lines[body_start:]:
        m = re.match(r"^## (.+)$", line)
        if m:
            if cur:
                sections.append(cur)
            title = m.group(1)
            num = int(re.match(r"^(\d+)\.", title).group(1))
            cur = (num, title, [])
        elif cur:
            cur[2].append(line)
    if cur:
        sections.append(cur)

    # nav
    nav = ['<nav id="toc" aria-label="Table of contents">', "<h2>Contents</h2>"]
    for group, lo, hi in NAV_GROUPS:
        nav.append(f'<div class="nav-group">{group}</div>')
        nav.append(f'<ol start="{lo}">')
        for num, title, _ in sections:
            if lo <= num <= hi:
                label = re.sub(r"^\d+\.\s*", "", title)
                nav.append(f'<li><a href="#{gh_slug(title)}">{inline(label)}</a></li>')
        nav.append("</ol>")
    nav.append("</nav>")

    # sections html
    secs = []
    for num, title, body in sections:
        secs.append(f'<section id="{gh_slug(title)}">')
        secs.append(f"<h2>{inline(title)}</h2>")
        secs.append(blocks_to_html(body))
        secs.append("</section>")

    pills_html = "\n".join(f'<span class="pill">{html_mod.escape(p)}</span>' for p in pills)

    doc = TEMPLATE.replace("{{TITLE}}", html_mod.escape(h1))
    doc = doc.replace("{{SUBTITLE}}", inline(subtitle))
    doc = doc.replace("{{PILLS}}", pills_html)
    doc = doc.replace("{{NAV}}", "\n".join(nav))
    doc = doc.replace("{{SECTIONS}}", "\n".join(secs))
    DST.write_text(doc)
    print(f"rendered {DST} ({len(doc)} bytes, {len(sections)} sections)")


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{TITLE}} — Master Documentation</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      color-scheme: light;
      --bg: #fdfaf4;
      --paper: #fffdfa;
      --ink: #07121e;
      --text: #101c28;
      --muted: #515f6e;
      --line: #e3ddd3;
      --soft: #f4f0e7;
      --soft-2: #f1eadc;
      --sand: #f1e3cb;
      --teal: #339797;
      --primary: #133555;
      --code-bg: #f4f0e7;
      --font-sans: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    * { box-sizing: border-box; }
    html { overflow-x: hidden; }
    body {
      margin: 0; background: var(--bg); color: var(--text);
      font-family: var(--font-sans);
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
      -webkit-font-smoothing: antialiased;
      line-height: 1.6; overflow-x: hidden;
    }
    a { color: var(--teal); text-decoration: none; }
    a:hover { text-decoration: underline; text-underline-offset: 3px; }
    .shell { display: grid; grid-template-columns: 280px minmax(0, 1fr); min-height: 100vh; }
    nav {
      position: sticky; top: 0; height: 100vh; overflow: auto;
      padding: 28px 22px; border-right: 1px solid var(--line); background: #faf5eb;
    }
    nav h2 {
      margin: 0 0 20px; font-family: var(--font-mono); font-size: 11px; font-weight: 500;
      letter-spacing: 0.14em; text-transform: uppercase; color: var(--teal);
    }
    nav ol { list-style: decimal; padding-left: 20px; margin: 0 0 18px; }
    nav li { margin: 8px 0; font-size: 13.5px; }
    nav a { color: var(--muted); }
    nav a:hover { color: var(--ink); text-decoration: none; }
    nav li::marker { color: var(--line); font-family: var(--font-mono); font-size: 11px; }
    .nav-group {
      margin: 20px 0 8px; font-family: var(--font-mono); color: var(--teal);
      font-size: 10px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase;
    }
    .nav-group:first-of-type { margin-top: 0; }
    main { min-width: 0; padding: 48px 56px 80px; }
    .document { max-width: 1120px; margin: 0 auto; background: var(--paper); border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
    header { padding: 54px 58px 38px; border-bottom: 1px solid var(--line); background: rgba(241, 227, 203, 0.4); }
    header p.kicker {
      margin: 0 0 14px; font-family: var(--font-mono); color: var(--teal); font-weight: 500;
      letter-spacing: 0.14em; text-transform: uppercase; font-size: 12px;
    }
    h1 { margin: 0; font-size: clamp(34px, 5vw, 56px); font-weight: 600; line-height: 1.05; letter-spacing: -0.02em; color: var(--ink); }
    .subtitle { margin: 22px 0 0; max-width: 820px; font-size: 18px; line-height: 1.6; color: var(--muted); }
    .meta { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 28px; }
    .pill {
      display: inline-flex; align-items: center; min-height: 28px; padding: 4px 12px;
      border: 1px solid var(--line); background: var(--paper); border-radius: 999px;
      color: var(--muted); font-family: var(--font-mono); font-size: 11px; font-weight: 500;
    }
    section { padding: 38px 58px; border-bottom: 1px solid var(--line); }
    section:last-child { border-bottom: 0; }
    h2 { margin: 0 0 18px; font-size: 28px; font-weight: 600; line-height: 1.15; letter-spacing: -0.02em; color: var(--ink); }
    h3 { margin: 28px 0 10px; font-size: 19px; font-weight: 600; line-height: 1.25; letter-spacing: -0.01em; color: var(--ink); }
    h4 { margin: 22px 0 8px; font-size: 15px; font-weight: 600; color: var(--ink); }
    p { margin: 0 0 14px; overflow-wrap: break-word; }
    .callout {
      margin: 22px 0; padding: 18px 20px; border: 1px solid var(--line);
      border-left: 3px solid var(--teal); border-radius: 6px; background: var(--soft);
    }
    .callout strong { color: var(--ink); }
    table { width: 100%; border-collapse: collapse; margin: 18px 0 26px; font-size: 14px; }
    th, td { vertical-align: top; text-align: left; padding: 11px 12px; border: 1px solid var(--line); overflow-wrap: break-word; }
    th {
      background: var(--soft-2); font-family: var(--font-mono); font-size: 11px; font-weight: 500;
      letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink);
    }
    ul, ol { margin: 8px 0 18px 22px; padding: 0; }
    li { margin: 6px 0; overflow-wrap: break-word; }
    code { padding: 2px 5px; border-radius: 4px; background: var(--code-bg); font-family: var(--font-mono); font-size: 0.88em; overflow-wrap: anywhere; }
    pre {
      overflow: auto; padding: 16px 18px; background: var(--code-bg);
      border: 1px solid var(--line); border-radius: 6px; line-height: 1.5; font-size: 12.5px; font-family: var(--font-mono);
    }
    pre code { padding: 0; background: transparent; }
    .diagram {
      white-space: pre; overflow: auto; padding: 18px; border: 1px solid var(--line);
      border-radius: 6px; background: var(--paper); font-family: var(--font-mono); font-size: 12.5px; line-height: 1.5;
    }
    #toc-toggle, #toc-backdrop { display: none; }
    @media (max-width: 960px) {
      .shell { display: block; }
      nav {
        position: fixed; top: 0; left: 0; bottom: 0; height: 100dvh;
        width: min(320px, 85vw); z-index: 50; background: #faf5eb;
        border-right: 1px solid var(--line);
        transform: translateX(-105%); transition: transform 0.25s ease;
      }
      body.toc-open nav { transform: none; }
      #toc-backdrop { position: fixed; inset: 0; z-index: 40; background: rgba(7, 18, 30, 0.4); }
      body.toc-open #toc-backdrop { display: block; }
      #toc-toggle {
        display: inline-flex; align-items: center; gap: 8px;
        position: fixed; bottom: 18px; right: 18px; z-index: 60;
        border: 0; border-radius: 6px; padding: 13px 18px;
        background: var(--primary); color: #ffffff;
        font-family: var(--font-mono); font-size: 11px; font-weight: 500;
        letter-spacing: 0.14em; text-transform: uppercase; cursor: pointer;
      }
      main { padding: 20px 16px 96px; }
      header { padding: 34px 20px 28px; }
      section { padding: 28px 20px; }
      table { display: block; overflow-x: auto; }
    }
    @media print {
      body { background: white; }
      .shell { display: block; }
      nav, #toc-toggle, #toc-backdrop { display: none !important; }
      main { padding: 0; }
      .document { border: 0; }
      section, header { break-inside: avoid; }
    }
  </style>
</head>
<body>
  <div id="toc-backdrop"></div>
  <button id="toc-toggle" type="button" aria-controls="toc" aria-expanded="false">Contents</button>
  <div class="shell">
{{NAV}}
    <main>
      <article class="document">
        <header>
          <p class="kicker">Master Documentation</p>
          <h1>{{TITLE}}</h1>
          <p class="subtitle">{{SUBTITLE}}</p>
          <div class="meta">
{{PILLS}}
          </div>
        </header>
{{SECTIONS}}
      </article>
    </main>
  </div>
  <script>
    (function () {
      var btn = document.getElementById("toc-toggle");
      var backdrop = document.getElementById("toc-backdrop");
      function setOpen(open) {
        document.body.classList.toggle("toc-open", open);
        btn.textContent = open ? "Close" : "Contents";
        btn.setAttribute("aria-expanded", open ? "true" : "false");
      }
      btn.addEventListener("click", function () {
        setOpen(!document.body.classList.contains("toc-open"));
      });
      backdrop.addEventListener("click", function () { setOpen(false); });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") setOpen(false);
      });
      document.querySelectorAll("nav a").forEach(function (a) {
        a.addEventListener("click", function () { setOpen(false); });
      });
    })();
  </script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
