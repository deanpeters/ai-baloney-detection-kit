# Freshness Ledger

**Tier:** 1 Chaos · *Is it real, and is it still true?*
**Decision this informs:** commit two engineers for one sprint to ship RoadmapGPT and demo it to the board on Nov 14; open a PM headcount conversation. · **Decision period:** now through the board demo, 2026-11-14 (28 days).
**As of (from the environment):** 2026-10-17 · **Mode / voice:** Context Dump, unattended · Product Coach

**Access limits:** closed synthetic fixture, assessed as supplied. The message is dated only "Monday 8:02 AM." The LinkedIn post and vendor slide are described, not attached. `app.py` was read, not run. It contains a hard-coded key (redacted). The model name `chatmodel-2023-preview` is fictional; its real deprecation status cannot be looked up, so it is assessed from its own label.

---

## 1. Earlier re-check triggers (if renewing a decision)

None. No earlier decision record was supplied; this is a first pass.

## 2. Ledger

| Claim | Published | Observed / experiment period | Retrieved | Effective / version | Perishable or durable, and why | Still applies to this decision? |
|---|---|---|---|---|---|---|
| C1 4,000 tickets | Message, "Monday" (undated) | Sample export: date missing (`app.py` line 9) | 2026-10-17 | Jira access: token "expired??" (`app.py` line 2) | Perishable. The ticket backlog changes weekly, and access depends on a live token. | No. The access it needs has already lapsed (line 2), and the export's age is unknown. |
| C2 Writes roadmap | — | "it worked yesterday" (`app.py` line 27); which yesterday is missing | 2026-10-17 | Model `"chatmodel-2023-preview"`, "the one from that tutorial" (`app.py` line 6) | Perishable. A 2023 *preview* model is the most perishable thing in the folder: previews are, by their label, not stable releases (INFERENCE from the name). Output from it says nothing about a current model. | Freshness unknown. The only run claimed is an undated "yesterday" on a 2023 preview. |
| C3 AI prioritization | — | Code as read today | 2026-10-17 | `priority()`, `app.py` lines 13–16 | Durable. A keyword counter does not spoil; it was wrong on day one. | Yes, as evidence of what the code does now. (Receipts already sifted out the claim.) |
| C4 −80% | 2024 (vendor keynote) | Missing. "Customer-reported, select design partners," no period given | Not retrieved (described only) | AI planning tools of 2024; not this tool | Perishable. Tool capability claims age with the tools, and it was never about our team. Two years and at least one model generation out of date (INFERENCE). | No. Stale, and from the wrong population. |
| C5 Customers begging | Message, undated | Missing | — | — | Perishable. Demand shifts with the market. | Freshness unknown; no evidence to date. |
| C6 Two CEOs | Message, undated | Pinehurst outing: date missing | — | — | Durable as an event (two conversations happened). Perishable as a signal of interest. | Yes, as "two conversations happened." Not as current demand. |
| C7 Competitor shipped | LinkedIn post: date missing | — | Not retrieved (no link) | — | Perishable. Competitor launches, pricing, and features change fast. | Freshness unknown. Undated is unknown, not false. |
| C8 Basically done | Message; README | Code as read today | 2026-10-17 | Depends on an expired Jira token (line 2) and a 2023 preview model (line 6) | The code is current evidence. What it depends on is already stale. | The evidence is fresh, and it shows a build resting on two lapsed conditions. |
| C9 2 engineers, 1 sprint | Message, Monday | — | — | — | Perishable. Estimates go stale as scope is discovered. | No estimate exists to be fresh. |
| C10 Nov 14 | Message, Monday | — | — | Board demo 2026-11-14 | Durable date; perishable plan. | 28 days from today. One sprint (ASSUMPTION: two weeks) fits only if work starts within two weeks and the C9 estimate holds. |
| C11 Totally secure | Message | Code as read today | 2026-10-17 | `app.py` lines 5, 21–24 | Durable risk. A key in source stays exposed wherever the file has been copied, until it is rotated. | Yes, as evidence. (Receipts already sifted out the claim.) |
| C12 Tested on real data | README | "it worked yesterday" (line 27); export date missing | 2026-10-17 | `chatmodel-2023-preview` | Perishable. | Freshness unknown. |
| C13 30 seconds | README | No timing | — | `timeout=30` (line 24) | Perishable (latency depends on the model and service). | No measurement to date. |
| C14 Frees PMs | Message | — | — | — | Perishable forecast. | No evidence to date. |
| C15 Headcount | Message | Rests on C4 (2024) | — | — | Perishable; inherits C4's 2024 date. | No. The number underneath it is stale. |

> A recent retrieval does not make an old observation current. Reading `app.py` today makes the code current evidence; it does not make "it worked yesterday" current.

## 3. What changed

| Item | Was (supported) | Now (supported) | Same scope? |
|---|---|---|---|
| Jira access | A token once worked (implied by line 2) | "API token expired?? ask IT" (line 2) | Same system; access lapsed |
| Model | `chatmodel-2023-preview`, from a tutorial (line 6) | Current status missing | Unknown: a 2023 preview cannot be assumed to behave, or exist, as it did |
| 80% figure | 2024 vendor keynote, select design partners | Nothing newer supplied | No: different tools, different teams, different year |
| Ticket data | A sample, export date missing (line 9) | 12 rows in `sample_tickets.csv` | No: 12 of ~4,000 |

## 4. Squares that go stale

| Square | Stale because | Refresh |
|---|---|---|
| Valuable | C5, C7 undated; C6's outing undated | Current customer requests; a dated, named competitor launch |
| Usable | Nothing to be stale; missing | (handled in later tiers) |
| Viable | C4 is a 2024 vendor number from other teams | Our own planning hours, measured now |
| Feasible | Expired Jira token (line 2); 2023 preview model (line 6); undated sample export (line 9); undated "it worked yesterday" (line 27) | New Jira token through IT; a current, supported model; a dated full export; a timed, logged run |

## 5. Re-check triggers for what stays in play

| Evidence | Re-check date or event trigger | Basis |
|---|---|---|
| Hard-coded key (redacted), `app.py` line 5 | Rotate today, before anything else | Durable exposure until rotated; standard credential practice (ASSUMPTION about policy; no policy supplied) |
| Board demo plan (C10) | 2026-10-31: if no engineering estimate and no real Jira export by then, the Nov 14 demo is of a sample, and should be framed that way | ASSUMPTION: two-week sprint, needing to start by Oct 31 |
| Model choice (C2, C8) | Before any run used as evidence; and on any provider deprecation notice | The model's own "preview" label (INFERENCE) |
| Jira export (C1, C12) | Re-pull before each roadmap cycle; date-stamp it | Backlog changes weekly (ASSUMPTION) |
| Competitor claim (C7) | Only if a named competitor and launch date appear | Undated source |

## 6. Rating and exits

**Check the Sell-By Date:** Mystery Meat
**Because:** almost nothing behind the decision carries a date. The one dated outside number (C4) is from 2024 and from other teams; the build depends on an expired token (line 2) and a 2023 preview model (line 6); the only run on record is "it worked yesterday" (line 27). Stale is not false, so most of these go back for a refresh rather than out.

| Claim | Exit | Refresh needed | What would change it |
|---|---|---|---|
| C1 | Send back | New Jira token; dated full export | A dated export of all tickets |
| C2 | Send back | Re-run on a current, supported model; keep the output | A dated output from a current model |
| C3 | Pass (freshness) | None; the code is current and durable | (Receipts exit stands: sifted out) |
| C4 | Send back | Measure our own planning hours now | A current, measured baseline for our team |
| C5 | Send back | Dated customer requests | Requests from the last two quarters (ASSUMPTION window) |
| C6 | Pass (as an event) | Ask when the outing was, if used as demand | (n/a) |
| C7 | Send back | Name, date, and link for the competitor launch | A dated launch page |
| C8 | Send back | Token, model, and export refreshed before "done" can be claimed | A working run on refreshed dependencies |
| C9 | Send back | An engineering estimate, dated | (n/a) |
| C10 | Send back | Estimate by 2026-10-31 | C9 fitting before Nov 14 |
| C11 | Pass (freshness) | Rotate the key regardless | (Receipts exit stands: sifted out) |
| C12 | Send back | Dated test output | (n/a) |
| C13 | Send back | Timed run | (n/a) |
| C14 | Send back | Current PM time study | (n/a) |
| C15 | Send back | Inherits C4's refresh | A current time study, then a separate decision |

**Chaos tier, combined (Receipts + Sell-By):** 15 entered. 1 passes (C6, as two conversations only). 7 sifted out by Receipts (C1, C3, C4, C7, C8, C11, C15). 7 sent back for receipts or a refresh (C2, C5, C9, C10, C12, C13, C14). Freshness sifted nothing out on its own.

**The code tells on him (the sharpest contradictions, for the card):**
1. "Reads all 4,000 Jira tickets" vs line 2 `# TODO hook up jira later` and line 10 `with open("sample_tickets.csv") as f:` (12 rows).
2. "AI-powered prioritization" vs line 16 `return text.count("urgent") * 10 + text.count("customer") * 5 + text.count("ai") * 20`.
3. "Totally secure. It runs on my laptop." vs line 5 (a hard-coded key, redacted), line 21 `str(top)` and line 23 `requests.post("https://api.example-llm.com/v1/complete", …)`: whole ticket rows, reporter emails and customer names included, leave the laptop.

**Human decision:** _recorded by the human_. In this unattended run, the claims go on to `bdk-labels` per the run instructions.
