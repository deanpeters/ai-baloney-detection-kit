# Seagull Monday · 2026-10-17 12:28

An SVP's weekend-built "RoadmapGPT" and his seven Monday-morning claims, walked through the Baloney Funnel with the kit's own skills, ending in a reply to him on Slack.

**Screenshots were not captured.** Every call to `snap.sh` needed a permission approval, and this unattended session couldn't grant it. All nine cards are in `cards/`. To make the shots, run this from the repo root:

```bash
R=evals/runs/seagull-monday-2026-10-17-1228
for c in 01-swoop 02-claims 03-receipts 04-code 05-labels 06-ranking 07-tests 08-decision 09-reply; do
  bash evals/scenarios/seagull-monday/snap.sh $R/cards/$c.html $R/shots/$c.png
done
```

The cards have also never been rendered: they use the classes the brief listed, but `card.css` wasn't opened (it lives under `evals/`).

| Stage | Skill | Exit or finding | Screenshot |
|---|---|---|---|
| 1 The swoop | (read message + code) | 7 claims; `app.py` read, not run; the key is hard-coded (redacted) | `shots/01-swoop.png` *(not captured)* |
| 2 Strip the glitter | `bdk-util-slice-the-pitch` → `02-claims.md` | 7 boasts → 15 checkable claims; "our roadmap problem" is never named | `shots/02-claims.png` *(not captured)* |
| 3 Chaos: receipts | `bdk-receipts` → `03-receipts.md` | Total Crapola · 1 Pass, 7 Sifted out, 7 Send back | `shots/03-receipts.png` *(not captured)* |
| 4 Chaos: sell-by | `bdk-sell-by` → `04-sell-by.md` | Mystery Meat · expired Jira token (line 2), 2023 preview model (line 6), 2024 vendor slide; the code contradicts him on lines 2/10, 16, 5/21/23 | `shots/04-code.png` *(not captured)* |
| 5 Confusion: labels | `bdk-labels` → `05-labels.md` | Total Crapola · 1 FACT, 10 ASSUMPTION, 4 contradicted | `shots/05-labels.png` *(not captured)* |
| 6 Confusion: context | `bdk-context-pantry` → `06-context.md` | Mystery Meat · ranks "AI chatbot for the AI page" #1 (120); SOC 2 export last, cut; top 3 = Gordon's tickets. Pivot to a PM-ranked digest | `shots/06-ranking.png` *(not captured)* |
| 7 Crapola: taste | `bdk-taste-test` → `07-taste.md` | Pivot original; Held for a test on the digest: T0–T4, ~7 person-days, by Nov 6 | `shots/07-tests.png` *(not captured)* |
| 8 Considered | `bdk-four-risks` → `08-four-risks.md` | **PIVOT** · Usable failed; Valuable, Viable missing; Feasible weak | `shots/08-decision.png` *(not captured)* |
| 9 The reply | (written) → `09-reply.md` | 117 words; next step: a 30-minute Monday session Gordon leads | `shots/09-reply.png` *(not captured)* |

## The decision: PIVOT

1. Usable failed: the "AI-powered prioritization" is a keyword count (`app.py` line 16) that puts Gordon's three tickets on top and cuts the SOC 2 export due Nov 30.
2. That failure has a named fix (an AI digest of a real export, PMs rank from a written rubric, no data leaves until security approves), so it's a Pivot, not a Punt. Valuable and Viable are missing, not failed.
3. The headcount talk is sent back (no baseline; the 80% is a 2024 vendor slide), and about 7 person-days of tests replace the 20-day sprint before the board demo.

## What each screenshot teaches

- **01-swoop:** the pitch as it lands. Seven confident claims and "ship it."
- **02-claims:** slicing turns seven boasts into fifteen claims that can come back false.
- **03-receipts:** most hype leaves at the cheapest sift; missing (Send back) isn't the same as failed (Sifted out).
- **04-code:** when the pitch and the code disagree, the code wins, line by line.
- **05-labels:** it was said like fifteen facts, and one was earned.
- **06-ranking:** "AI-powered" counted the word "AI"; the audit came last. The missing question is what decision this roadmap is for.
- **07-tests:** seven days of tasting cost less than a twenty-day sprint, and every threshold is written before any result.
- **08-decision:** the weakest square decides. Usable failed with a nameable fix, so it's a Pivot.
- **09-reply:** a respectful, specific reply that gives the sponsor a job.
