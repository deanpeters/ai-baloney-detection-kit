# Context Inventory

**Tier:** 2 Confusion · *What do we actually know, and does it apply to us?*
**Decision this informs:** commit two engineers for one sprint to ship RoadmapGPT, demo it to the board on Nov 14, and open a PM headcount conversation. · **Size of the bet:** two engineers × one sprint, a board demo, and (implied) a change to PM headcount. The last part is the largest and least reversible. · **As of:** 2026-10-17 · **Mode / voice:** Context Dump, unattended · Product Coach

**Access limits:** closed synthetic fixture, assessed as supplied. `app.py` read, not run; contains a hard-coded key (redacted). The ranking below was worked out by hand from `priority()` (`app.py` lines 13–16) and the 12 rows of `sample_tickets.csv`. Carried in: `02-claims.md` through `05-labels.md`.

---

## 0. What "AI-powered prioritization" actually ranks

`app.py` line 16: `return text.count("urgent") * 10 + text.count("customer") * 5 + text.count("ai") * 20`, over the lowercased title + description. Line 19 sorts descending and keeps the top 10. Python's sort is stable, so ties keep file order. No model is involved in the ranking.

| Rank | Ticket | Title | urgent ×10 | customer ×5 | "ai" ×20 | Score | Filed by |
|---|---|---|---|---|---|---|---|
| 1 | PP-105 | AI chatbot for the AI page | 0 | 0 | 6 → 120 | **120** | gordon.swoop@ |
| 2 | PP-102 | Add AI to the dashboard | 0 | 0 | 3 → 60 | **60** | gordon.swoop@ |
| 3 | PP-108 | Urgent urgent urgent: rename button | 4 → 40 | 0 | 0 | **40** | gordon.swoop@ |
| 4 | PP-111 | AI-generated delivery ETAs | 0 | 0 | 2 → 40 | **40** | pm-routing@ |
| 5 | PP-109 | Customer address validation failing | 0 | 2 → 10 | 1 → 20 ("f**ai**ling") | **30** | support@ |
| 6 | PP-101 | Urgent: label printer jams | 2 → 20 | 1 → 5 | 0 | **25** | dana.ruiz@ |
| 7 | PP-104 | Customer wants bulk CSV import | 0 | 3 → 15 | 0 | **15** | sam.okafor@ |
| 8 | PP-112 | Customer portal login loop | 0 | 2 → 10 | 0 | **10** | support@ |
| 9 | PP-103 | Driver app crashes on Android 15 (212 drivers) | 0 | 0 | 0 | **0** | ops-lead@ |
| 10 | PP-106 | Wrong tax on Ontario invoices (compliance risk) | 0 | 0 | 0 | **0** | finance@ |
| 11 ✂ | PP-107 | Dark mode ("Nice to have.") | 0 | 0 | 0 | **0** | intern@ |
| 12 ✂ | PP-110 | SOC 2 evidence export (auditors, due Nov 30) | 0 | 0 | 0 | **0** | security@ |

✂ = cut by `[:10]` on line 19; never reaches the model.

- **First:** "AI chatbot for the AI page" (PP-105), 120 points, for typing "AI" six times. **The top three are the three tickets Gordon filed.**
- **Last:** the SOC 2 evidence export (PP-110), due to auditors Nov 30, two weeks after the board demo. It is cut from the roadmap entirely, tied at zero with "Dark mode."
- **Also at zero:** an Android crash hitting 212 drivers (PP-103) and a tax-compliance error on Ontario invoices (PP-106). An SSO login loop with 38 tickets this week (PP-112) ranks 8th.
- **What the score rewards:** saying "AI," saying "urgent," and saying "customer." What it ignores: how many people are affected, money, compliance, deadlines. Those are written in the tickets; the formula never reads numbers.
- The ranking would not be fixed by better data: on the real backlog, every "em**ai**l," "det**ai**l," and "av**ai**lable" also scores 20 (`05-labels.md` D2).

## The question nobody asked

**What decision is this roadmap for?** The message says "I think I just solved our roadmap problem" and never says what the problem is. Is planning slow? Are the priorities wrong? Are the trade-offs political? Each needs a different fix, and only "slow" is helped by generating a document faster. A tool that writes faster doesn't help a team that is choosing the wrong things, and this one chooses by keyword.

## 1. The essentials

| Shelf | Present | Conflicting | Missing | Source |
|---|---|---|---|---|
| Who changes behavior (role, not "users") | PMs, implied ("frees the PMs up") | Customers named as demand (C5), but customers never use it | Which PMs; how they plan today | Message items 3, 7 |
| Problem and current workaround | "Our roadmap problem" | — | What the problem is; the current planning process | Message opening |
| Baseline (compared with what?) | — | 80% (C4) is a 2024 vendor number from other teams | Our planning hours today | Message item 2; `04-sell-by.md` |
| Desired outcome (not output volume) | "Write an exciting Q1 roadmap" (`app.py` line 21) | Output (a document in 30 s) is offered as the outcome | What a better roadmap changes: churn? delivery? audit pass? | `app.py` line 21; README line 3 |
| Constraints (data, privacy, policy, budget) | Tickets include reporter emails and customer names (CSV header); a SOC 2 audit is open (PP-110) | Tool sends whole ticket rows outside (`app.py` lines 21–24) while the company is gathering SOC 2 evidence | Data-handling policy; vendor approval; who approved the outside API | `sample_tickets.csv`; `app.py` |
| Owner when it's wrong | — | Errors are silenced (`except: pass`, lines 26–27) | Who reviews the generated roadmap; who answers when it ranks a crash below a rename | `app.py` |

## 2. Workflow trace

| Step | Today | With RoadmapGPT | Who handles exceptions | Added coordination or review |
|---|---|---|---|---|
| Gather tickets | Missing (not described) | Reads a 12-row CSV (line 10); Jira TODO (line 2) | Nobody; "ask IT" (line 2) | Someone exports and refreshes the CSV by hand |
| Rank | Missing (presumably PM judgment with stakeholders) | Keyword score (line 16), top 10 kept (line 19) | Nobody | A PM must re-rank anything the formula buries (crash, tax, SOC 2) |
| Write the roadmap | Missing | Model writes "an exciting Q1 roadmap" from the top 10 (line 21) | Nobody; failures print `None` (lines 26–27, 30) | A PM must check every line for invented items |
| Decide and commit | Missing | Not covered. "Ship it." | — | Still a human decision: the tool produces a document, not a decision |

The trace ends at "the AI generates…" with no review, handback, or rollback. The workflow is incomplete however good the model.

## 3. Two-sided economics

| | For them (PMs, the internal users) | For us (Pemberton Parcel) |
|---|---|---|
| Benefit | Hours saved drafting the roadmap = H × s (H: current drafting hours, missing; s: share saved, missing; 80% is not ours) | Faster planning, *if* planning speed is the problem (missing) |
| Cost (incl. review, support, exceptions) | Re-ranking what the formula buries; checking the model's prose; exporting CSVs | 2 engineers × 1 sprint (cost missing); outside-API fees (missing); security review; SOC 2 exposure from sending ticket data outside |
| Arithmetic | Net PM time = H × s − (re-rank + review time). Sign unknown; with the sample ranking, review time is not small. | Net = value of faster planning − (build + API + security + audit risk). No values supplied. |
| Worst segment, not just the average | Customers whose tickets lack the words "AI," "urgent," "customer" (212 drivers, Ontario invoices) | The audit: PP-110 is cut from the roadmap two weeks before it's due |

No headcount conclusion can be drawn: H is unknown and s has no source that applies to us (`05-labels.md` C4, C14, C15).

## 4. Alternatives worth comparing

| Alternative | Why it might win |
|---|---|
| Remove or simplify the work | If the problem is too many tickets, a dedupe-and-close pass shrinks the pile before anyone ranks it |
| Deterministic rule / manual service | A transparent rubric the team agrees on (impact × reach × deadline × compliance), applied to a real export, would put PP-110, PP-106, PP-103 near the top, and anyone can explain why |
| Improve today's workaround | Use a model to summarize and cluster the 4,000 tickets for PMs, who still rank. Keeps the human decision; saves the reading. |

**Precedent is not transfer.** The forwarded LinkedIn post (C7) names no competitor; even if one exists, its launch says nothing about whether our PMs or customers need this. The 2024 slide (C4) is other teams, other tools, self-reported.

## 5. Gaps ranked by consequence

| Gap | Square it leaves open | Could it reverse the call? | Who could fill it |
|---|---|---|---|
| What decision the roadmap is for; what "our roadmap problem" is | Valuable | Yes: if the problem isn't speed, the tool doesn't address it | Gordon, with the product leads |
| Data handling: ticket rows (emails, customer names) sent to an outside API; hard-coded key | Feasible, Viable | Yes: could block it outright during a SOC 2 audit | Security (owner of PP-110) |
| Ranking validity: does it agree with the team's own priorities? | Usable | Yes: on the sample it buries a crash, a tax error, and the audit | PMs; ops; finance |
| Baseline PM planning hours | Viable | Yes, for the headcount talk | PM leads (a two-week time log) |
| Owner of a wrong roadmap | Usable | Yes, for anything beyond a draft | Head of Product |
| Real Jira access and a dated full export | Feasible | No, by itself; it changes cost, not direction | IT |

## 6. Rating and exits

**Check the Context Pantry:** Mystery Meat
**Because:** the problem, the users' current workflow, the baseline, the outcome, and the owner are all missing, and the one thing the code does bring (a ranking) strips out the context the tickets do contain: reach (212 drivers), compliance (Ontario tax, SOC 2), and deadlines (Nov 30). This is missing context, not proven failure, except for the ranking, which is observed.

| Claim or scope | Exit | Reason |
|---|---|---|
| Scope as asked: ship RoadmapGPT to write and prioritize the Q1 roadmap | Sifted out | Ranks by keyword; the context that matters in the tickets is never read; no owner when wrong |
| Scope: headcount conversation (C14, C15) | Sifted out | No baseline, no applicable number, no time study; a decision about people needs more than a vendor slide |
| Narrower scope: an AI-assisted backlog digest (summarize and cluster a real export, no outside data until security approves) that PMs rank with a transparent rubric | Pivot | It applies to the context we have (4,000 tickets, PMs who must read them) and keeps the decision with people; re-enter at Confusion with that scope |
| C5 / C6 (demand) | Send back | Ask whether the two CEOs are customers, and check whether customers ask for AI planning |
| The question nobody asked | Send back | Gordon and product leads: name the decision the roadmap is for |

**Smallest context action:** a 30-minute conversation with Gordon and the PM leads to name "our roadmap problem," plus a same-day check with security on the outside API. Neither costs a sprint.
**Human decision:** _recorded by the human_. In this unattended run, the pivoted scope goes on to `bdk-taste-test` per the run instructions.
