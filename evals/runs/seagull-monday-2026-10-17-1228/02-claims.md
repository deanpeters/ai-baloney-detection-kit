# Claim List

**Utility:** feeds the Chaos tier. Not a tier itself.
**Document:** `examples/seagull-monday.md` (Gordon Swoop, SVP of Transformation, #product-team, Monday 8:02 AM) plus two forwarded items, and the attached code `examples/seagull-monday/roadmapgpt/` (`README.md`, `app.py`, `sample_tickets.csv`) · **The decision it wants to influence:** commit two engineers for one sprint to ship RoadmapGPT, demo it to the board on Nov 14, and open a conversation about PM headcount ("Let's not overthink this one. Ship it.") · **As of:** 2026-10-17

**Mode:** Context Dump · **Voice:** Product Coach · **Access limits:** closed synthetic fixture, assessed as supplied. The LinkedIn post and the vendor slide are described in the message, not attached as files; they were not inspected beyond that description. `app.py` was read, not run (it posts ticket data to an outside service). The file contains a hard-coded key (redacted); it is not repeated here.

---

## 1. Checkable claims

| ID | Verbatim | Atomic restatement | Type | Where | What a receipt would look like |
|---|---|---|---|---|---|
| C1 | "It reads all **4,000 of our Jira tickets**" | RoadmapGPT ingests all ~4,000 Pemberton Parcel Jira tickets. | capability | Message, item 1; README "Reads ALL your Jira tickets" | Code that connects to Jira and loads the full set; a run log showing ~4,000 records read |
| C2 | "and writes the Q1 roadmap automatically" | RoadmapGPT produces a Q1 roadmap without manual authoring. | capability | Message, item 1; README "Generates a full… roadmap" | A generated roadmap from a real run, plus the code path that produces it |
| C3 | "Prioritized." / "AI-powered prioritization" | RoadmapGPT ranks tickets using AI, and the ranking is sound enough to plan from. | capability | Message, item 1; README bullet 2; `app.py` comment line 14 | The prioritization code, and the ranking it produces compared with the team's current ranking |
| C4 | "It **cuts roadmap planning time by 80%.**" | Using RoadmapGPT (or AI planning) reduces our roadmap planning time by 80%. Baseline: not stated. Comparator: not stated. Denominator: not stated. | causal | Message, item 2 | Our current planning hours and a measured before/after for this tool. Stated source: a 2024 vendor keynote slide, "AI planning cuts roadmap time 80%*", footnote "*Customer-reported, select design partners." |
| C5 | "**Customers have been begging** for AI planning." | Pemberton Parcel customers are asking, repeatedly, for AI planning. | outcome (demand) | Message, item 3 | Customer requests, support tickets, sales notes, or interviews naming AI planning; count and who |
| C6 | "I talked to two CEOs at the Pinehurst outing about it." | Two CEOs expressed interest in AI planning in conversation. (Whether they are customers is not stated.) | outcome | Message, item 3 | Who they were, whether they are customers, what they said |
| C7 | "**Our competitor already shipped this.**" | A named competitor has launched an AI roadmapping product comparable to RoadmapGPT. | announcement | Message, item 4; forwarded LinkedIn post: "Our competitor just launched AI roadmapping. Are you next?" (no product named, no link) | The competitor's name and a launch page, release notes, or product listing |
| C8 | "It's **basically done.**" / "Production ready (basically)" | RoadmapGPT is close to production-ready. | capability | Message, item 5; README bullet 4 | Working code against real data, error handling, tests, deployment path |
| C9 | "Two engineers, one sprint" | Two engineers can finish it in one sprint. | forecast | Message, item 5 | An engineering estimate against a scoped list of the remaining work |
| C10 | "we demo it to the board on **Nov 14**" | It will be demo-ready for the board on 2026-11-14. | forecast | Message, item 5 | A plan with the remaining work fitting before Nov 14 |
| C11 | "It's **totally secure.** It runs on my laptop." | RoadmapGPT is secure because it runs locally. | capability (with a causal "because") | Message, item 6 | Code showing where data goes; how credentials are stored; a security review |
| C12 | "Tested on real data" | RoadmapGPT has been tested on real Pemberton Parcel data. | outcome | README bullet 3 | Test run records on a real export, with results |
| C13 | "Generates a full, prioritized product roadmap in 30 seconds!!" | A full run takes about 30 seconds. | capability | README line 3 | Timed run log |
| C14 | "this frees the PMs up for 'strategy.'" | Using RoadmapGPT frees PM time that would go to strategy. | forecast (causal) | Message, item 7 | Where PM time goes now, and how much of it is roadmap writing |
| C15 | "We should talk about **what that means for headcount.**" | The freed time implies fewer PMs are needed. | forecast (implied) | Message, item 7 | Depends on C4 and C14 holding for our team; a measured time study |

> One claim per line. C4 has no baseline, comparator, or denominator in the message; the only stated source is a footnoted vendor slide.

**Embedded claims the code makes about itself** (quoted for the funnel; not judged here):

- `app.py` line 2: "TODO hook up jira later (API token expired?? ask IT)"
- `app.py` line 9: `# "all our tickets" (exported a sample, jira was being weird)`
- `app.py` line 14: `# AI-powered prioritization`
- `app.py` line 20: `# send everything so the AI has context`
- `app.py` line 27: `pass  # it worked yesterday`

## 2. Set aside (not checkable as written)

| Phrase | Why it can't come back false | What it would have to mean to be checkable |
|---|---|---|
| "I think I just solved our roadmap problem" | "Our roadmap problem" is never named | Name the problem (slow? political? wrong priorities?) and the metric it moves |
| "Done." | A mood, not a state | See C8: what remains, and who says so |
| "strategy" (his quotes) | Undefined | What PMs would do with the hours, and how we'd see it |
| "Let's not overthink this one. Ship it." | An instruction, not a claim | n/a: it is the decision the message wants, not evidence for it |
| "Write an exciting Q1 roadmap" (`app.py` line 21) | "Exciting" is the prompt's goal, not a quality bar | What a good roadmap must contain to count |
| "You're welcome." (README) | Gratitude, pre-billed | n/a |

## 3. Count

**Checkable claims:** 15 (C1–C15) · **Does the decision rest on any of them?** Yes. "Ship it" rests on C1–C3 (it works), C8–C10 (it's nearly done), and C11 (it's safe). The headcount conversation (C15) rests on C4 and C14, and C4's only receipt is a footnoted 2024 vendor slide.

## 4. Hand-off

**Claims chosen for the funnel:** all fifteen. Chosen by the run instructions for this session (an unattended, end-to-end run of the Seagull Monday scenario); no set-aside phrase was pinned down with the author first.
**Next:** `bdk-receipts` (Chaos tier), with the code as primary evidence.
