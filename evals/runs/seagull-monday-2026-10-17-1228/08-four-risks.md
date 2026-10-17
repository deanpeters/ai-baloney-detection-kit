# Four-Risk Grid and Decision Record

**Tier:** 4 Considered · *Pursue, pivot, or punt?*
**The bet:** RoadmapGPT, Gordon Swoop's weekend prototype that is said to read all Jira tickets and write a prioritized Q1 roadmap; and its pivot, an AI-assisted backlog digest that PMs rank with a written rubric. · **As of:** 2026-10-17 · **Mode / voice:** Context Dump, unattended · Product Coach

**Access limits:** closed synthetic fixture. `app.py` read, not run; it contains a hard-coded key (redacted). Evidence carried in from `02-claims.md` through `07-taste.md`; no test has been run.

**Scopes on the table** (each gets its own move):
1. Ship RoadmapGPT as built: two engineers × one sprint to finish it.
2. Board demo on Nov 14 of "AI writes our roadmap."
3. A PM headcount conversation.
4. The pivot: ~7 person-days of tests (T0–T4 in `07-taste.md`) on an AI-assisted backlog digest.

---

## 1. The grid

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **VALUABLE**<br>"Is this something someone would buy?" (internal tool: would PMs choose it over what they do now?)<br><br>Status: **missing**<br>Evidence: two conversations with CEOs at a golf outing (C6, FACT, narrow); "customers have been begging" (C5) and "competitor already shipped" (C7) are ASSUMPTIONs with no receipt; no PM asked; "our roadmap problem" never named<br>Scale: Mystery Meat | **VIABLE**<br>"Is this good business?" (Is there ROI for both sides?)<br><br>Their ROI (PMs): **missing**. Hours saved unknown; re-ranking and review time unknown; on the sample, review would be heavy<br>Our ROI: **missing**. 2 engineers × 1 sprint, model fees, security review, and audit exposure unpriced; the only benefit number is a 2024 vendor slide from other teams (C4, sifted out)<br>Status: **missing**<br>Scale: Mystery Meat |
| **Can we?** | **USABLE**<br>"Will users trust and adopt it?"<br><br>Status: **failed** (keyword ranking) · **missing** (digest)<br>Evidence: `app.py` line 16 ranks by counting "urgent," "customer," and "ai." On the sample, #1 is "AI chatbot for the AI page" (120); the top three are Gordon's own tickets; the SOC 2 export (due Nov 30), the Ontario tax error, and an Android crash hitting 212 drivers score 0, and SOC 2 is cut. A PM can't defend that ranking, so would re-rank all of it.<br>Scale: Total Crapola (ranking) | **FEASIBLE**<br>"Can we even do this with what we know and have?"<br><br>Status: **weak**<br>Evidence: reads a 12-row sample, not 4,000 tickets (line 10); Jira token expired (line 2); 2023 preview model (line 6); errors swallowed (lines 26–27); whole ticket rows, with reporter emails and customer names, posted to an outside API (lines 21–24) with a hard-coded key, redacted (line 5), during an open SOC 2 audit. All fixable; none fixed.<br>Scale: Real Imitation Baloney |

Status: earned · weak · missing · stale · failed
**Feasible-only flag:** ☑ the only evidence is a working demo. *AI made building cheap. The demo proves buildable, not feasible.* Here it proves less than that: it reads a sample, ranks by keyword, and sends data outside.

## 2. Moves

| Scope | Move | Deciding square | Why |
|---|---|---|---|
| 1. Ship RoadmapGPT as built (2 eng × 1 sprint) | **Pivot** (not earned as asked) | Usable (failed) | A Can-we square failed on a nameable thing: keyword ranking. Fix: the model summarizes and clusters, PMs rank with a written rubric, and nothing leaves the building until security approves. Never Punt a fixable Usable failure. |
| 2. Board demo, Nov 14, "AI writes our roadmap" | **Pivot** | Usable, Feasible | The demo as framed would show a 12-ticket sample ranked by keyword. Pivot the demo: show the digest on a real export, the rubric, and T1–T4 results with their thresholds. That is a stronger board story than a claim the code can't back. |
| 3. PM headcount conversation | **Send back** (not earned) | Viable (missing) | No baseline, no applicable number, no time study. Missing, not failed: it waits for T3's time log, and then it is a separate decision about people, not a by-product of a tool. |
| 4. Digest tests T0–T4 (~7 person-days) | **Pursue** the cheapest test | Valuable, Usable (missing) | Squares missing, not failed: Pursue the cheapest test. About a third of the sprint asked for, done before Nov 14. |

**Overall move for the bet: PIVOT.** No averages. The weakest square decides, and the weakest square is Usable: a ranking that puts "rename button" above the audit.

**Alternatives a reasonable person might choose:**
- **Ship as asked.** Cost: a sprint spent hardening a keyword counter; a board demo that recommends dropping the SOC 2 export two weeks before it's due; ticket data with customer names sent to an unapproved service during an audit.
- **Punt entirely.** Cost: loses a sponsor's energy and a plausible digest idea that seven days could settle. Not supported: Valuable is missing, not failed.
- **Send everything back and wait.** Cost: Nov 14 arrives with nothing to show. The pivot gives the board real results instead.

## 3. Decision record

| | |
|---|---|
| Recommended move and scope | **Pivot** RoadmapGPT into an AI-assisted backlog digest that PMs rank with a written rubric; **Pursue** tests T0–T4 (~7 person-days); **Send back** the headcount conversation; pivot the Nov 14 demo to show the digest and test results |
| Deciding squares and evidence | Usable failed: `app.py` line 16 and the hand replay (`06-context.md` §0). Feasible weak: lines 2, 5, 6, 10, 21–24, 26–27. Valuable and Viable missing: C5, C7, C4 unsupported or sifted out |
| Suggested owner role | Product lead (T1, overall); a PM who didn't build it (T2); Head of Product (T3); security (T0); one engineer (T4). Gordon as executive sponsor: he owns the "what problem are we solving" conversation and the board story |
| By when | T0 today; T1 and T3 start Monday; all results by 2026-11-06, a week before the board demo |
| What would change the call | T1: fewer than 2 of 5 PMs name triage as a real cost → Punt the digest. T2: compliance/safety tickets dropped or invented tickets → Pivot again or Punt. T3: triage under 10% of planning hours → Punt the build, keep the rubric. Security says no outside route → Feasible fails; Pivot to an approved internal model or Punt |
| Where it goes next | Back in at Confusion (`bdk-context-pantry`) with the digest scope, then Crapola (`bdk-taste-test`) to review T1–T4 results |
| Re-check triggers (perishable evidence) | Model choice: before any run used as evidence, and on any deprecation notice. Jira export: re-pull and date-stamp each planning cycle. Board demo plan: 2026-10-31 checkpoint. SOC 2 deadline 2026-11-30 |
| Hand-off (if any) | An executive's weekend prototype: `pant-executive-decision-review` (Product Manager Antagonist Skills). Not run here |
| **Human decision** | _recorded by the human, not the assistant_ |
