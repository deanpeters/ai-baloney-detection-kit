#!/usr/bin/env python3
"""Turn a finished Seagull Monday run folder into session.html (scroll it on stage) and transcript.md.
Usage: python3 evals/scenarios/seagull-monday/build-session.py evals/runs/seagull-monday-<stamp>
"""
import glob, html, json, os, re, sys

run = sys.argv[1].rstrip("/")
esc = html.escape

# transcript.jsonl (claude -p --output-format stream-json) → transcript.md: what the agent said and which tools it used.
lines = []
tj = os.path.join(run, "transcript.jsonl")
if os.path.exists(tj):
    for raw in open(tj):
        try: ev = json.loads(raw)
        except ValueError: continue
        if ev.get("type") == "assistant":
            for c in ev.get("message", {}).get("content", []):
                if c.get("type") == "text" and c["text"].strip(): lines.append(c["text"].strip() + "\n")
                elif c.get("type") == "tool_use":
                    inp = c.get("input", {})
                    what = inp.get("skill") or inp.get("command") or inp.get("file_path") or inp.get("pattern") or ""
                    lines.append(f"> **{c['name']}** `{str(what)[:140]}`\n")
        elif ev.get("type") == "result":
            lines.append(f"\n---\nDone in {ev.get('duration_ms', 0) / 1000:.0f}s, {ev.get('num_turns', '?')} turns.\n")
    open(os.path.join(run, "transcript.md"), "w").write("# Transcript\n\n" + "\n".join(lines))

def md(text):
    """Just enough Markdown for skill output: headings, bold, code, lists, tables, paragraphs."""
    out, in_code, table = [], False, []
    def inline(s):
        s = esc(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
        return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    def flush():
        if table:
            rows = [r for r in table if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
            out.append("<table>" + "".join("<tr>" + "".join(f"<td>{inline(c.strip())}</td>" for c in r.strip().strip("|").split("|")) + "</tr>" for r in rows) + "</table>")
            table.clear()
    for ln in text.splitlines():
        if ln.startswith("```"):
            flush(); out.append("</pre>" if in_code else "<pre>"); in_code = not in_code; continue
        if in_code: out.append(esc(ln)); continue
        if ln.strip().startswith("|"): table.append(ln); continue
        flush()
        m = re.match(r"^(#{1,4})\s+(.*)", ln)
        if m: out.append(f"<h{len(m.group(1)) + 2}>{inline(m.group(2))}</h{len(m.group(1)) + 2}>")
        elif re.match(r"^\s*[-*]\s+", ln): out.append(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', ln))}</li>")
        elif re.match(r"^\s*\d+\.\s+", ln): out.append(f"<li>{inline(re.sub(r'^\s*\d+\.\s+', '', ln))}</li>")
        elif ln.strip(): out.append(f"<p>{inline(ln)}</p>")
    flush()
    return "\n".join(out)

stages = sorted(f for f in glob.glob(os.path.join(run, "[0-9][0-9]-*.md")))
shots = {os.path.basename(s)[:2]: s for s in sorted(glob.glob(os.path.join(run, "shots", "*.png")))}
parts = []
if os.path.exists(os.path.join(run, "SESSION.md")):
    parts.append(f'<section class="summary">{md(open(os.path.join(run, "SESSION.md")).read())}</section>')
done = set()
for f in stages:
    n = os.path.basename(f)[:2]
    shot = shots.get(n)
    img = f'<img src="shots/{os.path.basename(shot)}" alt="">' if shot else ""
    if shot: done.add(n)
    parts.append(f'<section><div class="num">{n}</div>{img}<details{" open" if not shot else ""}><summary>{esc(os.path.basename(f))}: the skill output</summary>{md(open(f).read())}</details></section>')
for n, shot in shots.items():   # cards without a stage file (01-swoop)
    if n not in done:
        parts.insert(1 if parts and 'summary' in parts[0] else 0, f'<section><div class="num">{n}</div><img src="shots/{os.path.basename(shot)}" alt=""></section>')

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Seagull Monday Session</title><style>
:root{{--bg:#0b0b0b;--card:#161616;--fg:#f2f2f2;--mute:#9a9a9a;--green:#00E874;--line:#2a2a2a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
main{{max-width:1240px;margin:0 auto;padding:32px 16px 80px}}h1{{font-size:34px;margin:0}}h1 span{{color:var(--green)}}.lede{{color:var(--mute)}}
section{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:0 0 18px;position:relative}}
.num{{position:absolute;top:12px;left:16px;font-weight:800;color:var(--green);font-size:22px}}
img{{display:block;width:100%;border-radius:8px;border:1px solid var(--line);margin-top:28px}}
summary{{cursor:pointer;color:var(--mute);margin-top:12px}}table{{border-collapse:collapse;width:100%;margin:8px 0}}td{{border:1px solid var(--line);padding:6px 10px;vertical-align:top}}
pre{{background:#000;padding:12px;border-radius:8px;overflow-x:auto}}code{{color:var(--green)}}h3,h4,h5{{color:var(--green)}}.summary{{border-color:var(--green)}}
a{{color:var(--green)}}
</style></head><body><main>
<h1>Seagull Monday: <span>RoadmapGPT</span></h1>
<p class="lede">An AI Baloney Detection Kit session, recorded {esc(os.path.basename(run))}. Fictional SVP, fictional company, real skills. <a href="transcript.md">Full transcript</a> · <a href="transcript.jsonl">raw</a></p>
{''.join(parts)}
</main></body></html>"""
open(os.path.join(run, "session.html"), "w").write(page)
print("wrote", os.path.join(run, "session.html"), f"({len(stages)} stages, {len(shots)} screenshots)")
