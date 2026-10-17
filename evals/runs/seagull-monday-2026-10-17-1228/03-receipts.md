## Show Me the Receipts: RoadmapGPT (Gordon's Monday message + the code)  ·  15 claims → 1 pass

- C1 Reads all 4,000 Jira tickets: SIFTED OUT · code opens a 12-row sample CSV
- C2 Writes the Q1 roadmap: SEND BACK · fetch one real generated roadmap
- C3 AI-powered prioritization: SIFTED OUT · ranking is a keyword count
- C4 Planning time cut 80%: SIFTED OUT · vendor slide, customer-reported, no method
- C5 Customers begging for AI planning: SEND BACK · fetch actual customer requests
- C6 Talked to two CEOs: PASS · first-hand; proves conversations, not demand
- C7 Competitor already shipped: SIFTED OUT · no competitor, product, or link
- C8 Basically done: SIFTED OUT · Jira unhooked, errors swallowed, key hard-coded
- C9 Two engineers, one sprint: SEND BACK · get an engineering estimate
- C10 Board-ready Nov 14: SEND BACK · depends on C9's estimate
- C11 Totally secure, runs locally: SIFTED OUT · posts ticket data to outside service
- C12 Tested on real data: SEND BACK · fetch test results; none in folder
- C13 Roadmap in 30 seconds: SEND BACK · no timing; 30s is the timeout
- C14 Frees PMs for strategy: SEND BACK · fetch where PM time goes now
- C15 Fewer PMs needed: SIFTED OUT · rests on sifted-out C4

**Receipts:** Total Crapola · the attached code contradicts five of the claims it was sent to prove.

**Claim:** "It reads all 4,000 of our Jira tickets and writes the Q1 roadmap automatically. Prioritized."
**Challenge:** Show me the line that reads Jira.
**Evidence:** `app.py` line 10 opens a 12-ticket sample CSV.
**Better decision:** Drop "4,000"; demo only what the code does.

Say "full report" for the ledger, origin groups, and exits.

---

*Full report follows (this run is an unattended assessment that asks for the complete output).*

# Receipts Ledger

**Tier:** 1 Chaos · *Is it real, and is it still true?*
**Decision this informs:** whether to commit two engineers for one sprint to ship RoadmapGPT, demo it to the board on Nov 14, and open a PM headcount conversation.
**As of:** 2026-10-17 · **Mode / voice:** Context Dump, unattended · Product Coach · **Access limits:** closed synthetic fixture, assessed as supplied. The LinkedIn post (S5) and vendor slide (S6) are described in the message but not attached; only that description was inspected. `app.py` was read line by line, not run (running it would send ticket data to an outside service). It contains a hard-coded key (redacted). No Jira access, no customer records, no test output, no run logs were supplied.

---

## 1. Claims

From `02-claims.md`; IDs reused.

| ID | Claim (one atomic statement) | Announcement or outcome? |
|---|---|---|
| C1 | RoadmapGPT ingests all ~4,000 Jira tickets. | capability |
| C2 | It produces a Q1 roadmap automatically. | capability |
| C3 | It ranks tickets with AI, soundly enough to plan from. | capability |
| C4 | It cuts our roadmap planning time by 80%. | causal outcome |
| C5 | Customers have been begging for AI planning. | outcome (demand) |
| C6 | Gordon talked to two CEOs at the Pinehurst outing about it. | outcome (an event) |
| C7 | Our competitor already shipped this. | announcement |
| C8 | It's basically done / production ready. | capability |
| C9 | Two engineers can finish it in one sprint. | forecast |
| C10 | It will be board-demo-ready on Nov 14. | forecast |
| C11 | It's totally secure because it runs on Gordon's laptop. | capability |
| C12 | It was tested on real data. | outcome |
| C13 | It generates the roadmap in 30 seconds. | capability |
| C14 | It frees PMs up for "strategy." | forecast |
| C15 | That means fewer PMs (headcount). | forecast |

## 2. Sources

| Source | Location | Owner / publisher | Dates (published · observed) | Inspected or only supplied? | Supports which claim, and only what? |
|---|---|---|---|---|---|
| S1 | `examples/seagull-monday.md`, the message, items 1–7 | Gordon Swoop (sponsor; interested party) | Monday 8:02 AM · read 2026-10-17 | Inspected | That Gordon makes C1–C15. FACT about the message, not about the product. First-hand for C6 only. |
| S2 | `roadmapgpt/app.py`, lines 1–30 | Gordon (author) | weekend build · read 2026-10-17 | Inspected (read, not run) | What the code does. Primary evidence for C1, C2, C3, C8, C11, C13. |
| S3 | `roadmapgpt/README.md`, lines 1–12 | Gordon (author) | weekend build · read 2026-10-17 | Inspected | That the README repeats C1, C3, C8, and adds C12, C13. Same origin as S1. |
| S4 | `roadmapgpt/sample_tickets.csv`, 12 data rows (PP-101 to PP-112) | Gordon's export | export date not stated · read 2026-10-17 | Inspected | The data the code actually reads. Supports C1 (contradicts), C11 (what fields leave the laptop), C12 (what "real data" is). |
| S5 | Forwarded LinkedIn post: "Our competitor just launched AI roadmapping. Are you next?" | A growth consultant | not stated · not observed | Only supplied (described in S1; no link, no product named) | That a consultant posted it. Nothing about any competitor. |
| S6 | Forwarded 2024 vendor keynote slide: "AI planning cuts roadmap time 80%*", footnote "*Customer-reported, select design partners." | A vendor (AI Planning Summit, 2024) | 2024 · not observed | Only supplied (described in S1) | That a vendor showed the number. Not that anyone's time fell 80%, and not ours. |

## 3. Origin groups

| Origin | Sources that trace back to it | Independent evidence count |
|---|---|---|
| Gordon's own account | S1 (message), S3 (README) | 1, interested party. The README restating the message adds no corroboration. |
| The code and its sample data | S2, S4 | 1, primary and authoritative for what the code does |
| Growth consultant's post | S5 | 1, interested party, untraceable claim |
| Vendor keynote | S6 | 1, interested party, self-reported by "select design partners" |

> The message and README are one origin. The only independent, authoritative record in hand is the code, and it disagrees with the message.

## 4. Authority and method

| Claim | Best origin | Sample · denominator · baseline · incentives | Fit for this decision? |
|---|---|---|---|
| C1 4,000 tickets | S2 lines 2, 9–11; S4 | Line 2: `# TODO hook up jira later (API token expired?? ask IT)`. Line 10: `with open("sample_tickets.csv") as f:`. Line 9: `# "all our tickets" (exported a sample, jira was being weird)`. S4 has 12 rows. Denominator: 12 of ~4,000 (0.3%). | Authoritative, and it contradicts C1. |
| C2 Writes the roadmap | S2 lines 18–27 | Code builds a prompt and posts the top 10 to `https://api.example-llm.com/v1/complete` (lines 21–24). On any error, line 26–27 `except: pass  # it worked yesterday` returns nothing, so `print` shows `None` (line 30). No output was supplied. | Shows an attempt, not a roadmap. Missing. |
| C3 AI prioritization | S2 lines 13–16, 19 | Line 16: `return text.count("urgent") * 10 + text.count("customer") * 5 + text.count("ai") * 20`. Line 19 sorts by that before any model is called. The model only writes prose about tickets already chosen. | Authoritative, and it contradicts "AI-powered." It is a keyword counter. |
| C4 −80% | S6 | Customer-reported; select design partners; no baseline, no method, no denominator; vendor incentive; about AI planning in general, not this tool. | Interested party, no method, consequential decision (headcount). Not fit. |
| C5 Customers begging | S1 item 3 | Only supporting detail is C6. No tickets, sales notes, or interviews supplied. Of the 12 sample tickets, the two AI requests (PP-102, PP-105) were filed by Gordon; none asks for AI planning. | Missing. (The sample is 12 rows, so absence there is not proof of absence.) |
| C6 Two CEOs | S1 item 3 | First-hand report of two conversations at a golf outing. Whether they are customers, and what they said, not stated. | Fit only for "two conversations happened." |
| C7 Competitor shipped | S5 | No competitor or product named, no link. Author sells growth consulting; the post is a call to fear ("Are you next?"). | Nothing to check. Not fit. |
| C8 Basically done | S2 | Jira not connected (line 2); sample file (line 10); hard-coded key (line 5, redacted); model pinned to `"chatmodel-2023-preview"` "the one from that tutorial" (line 6); bare `except: pass` (lines 26–27); prompt asks for "an exciting Q1 roadmap" (line 21). No tests, no config, no deployment. | Authoritative, and it contradicts C8. |
| C9 2 engineers, 1 sprint | S1 item 5 | Sponsor's forecast; no scope, no engineering estimate. | Missing. |
| C10 Nov 14 | S1 item 5 | The date is Gordon's to set; readiness depends on C9. | Missing. |
| C11 Totally secure | S2 lines 5, 19–24; S4 header | Line 5 holds a hard-coded key (redacted) with `# TODO move this somewhere`. Line 21 `str(top)` serializes whole ticket rows, including `reporter_email` and `customer` (S4 header), and line 23 posts them to an outside API. "Runs on my laptop" is true of the script and irrelevant to where the data goes. | Authoritative, and it contradicts C11. |
| C12 Tested on real data | S2 line 9, 27; S3 line 7 | "Exported a sample." The only test record in the folder is the comment `# it worked yesterday`. The sample uses `example.com` addresses; whether it is real production data is not established. | Missing. |
| C13 30 seconds | S3 line 3; S2 line 24 | No timing log. `timeout=30` (line 24) is the most the request may take before it fails silently. | Missing. |
| C14 Frees PMs | S1 item 7 | No measure of PM time now or after. Depends on C2 and C4. | Missing. |
| C15 Headcount | S1 item 7 | Rests on C4 (sifted out) and C14 (missing). | Not fit for a decision about people's jobs. |

## 5. Contradictions

| Claims | What disagrees | Scope / period / method difference | Resolved? |
|---|---|---|---|
| C1 vs S2 line 10, S4 | "All 4,000 Jira tickets" vs a 12-row CSV; Jira "TODO" (line 2) | Same tool, same weekend | Yes: the code wins. 12 tickets. |
| C3 vs S2 line 16 | "AI-powered prioritization" vs keyword counts of "urgent," "customer," "ai" | Same function | Yes: the code wins. No model ranks anything. |
| C8 vs S2 lines 2, 5, 6, 26–27 | "Basically done" vs unconnected Jira, hard-coded key (redacted), 2023 preview model, swallowed errors | Same build | Yes: the code wins. |
| C11 vs S2 lines 5, 21–24 | "Totally secure, runs on my laptop" vs ticket rows (with reporter emails and customer names) posted to an outside API with a key in the source | Same build | Yes: the code wins. |
| C13 vs S2 line 24 | "30 seconds" vs a 30-second timeout followed by `except: pass` | Same request | Unresolved: no timing exists; 30 s is the failure ceiling, not a measured run. |

## 6. Four-risk squares informed

| Square | Receipts that bear on it | Status |
|---|---|---|
| Valuable: "Is this something someone would buy?" | C5 (missing), C6 (two conversations), C7 (sifted out) | missing |
| Usable: "Will users trust and adopt it?" | None. No PM has used it; C3 shows a ranking a PM could not defend. | missing |
| Viable: "Is this good business?" | C4 (sifted out), C14 (missing), C15 (sifted out) | missing |
| Feasible: "Can we even do this with what we know and have?" | C1, C3, C8, C11 contradicted; C9 missing | weak. **Feasible-only flag:** the only evidence is a weekend prototype, and it proves less than claimed. |

## 7. Rating and exits

**Show Me the Receipts:** Total Crapola
**Because:** the one authoritative, independent record supplied (the code) directly contradicts C1, C3, C8, and C11, and the two outside receipts (S5, S6) are interested parties with no method. Missing evidence (C5, C9, C12–C14) is not dishonesty and is sent back, not failed.

| Claim | Exit | Reason | What would change it |
|---|---|---|---|
| C1 | Sifted out | Code reads 12 sample rows (line 10); Jira is a TODO (line 2) | A run log showing the Jira connection and ~4,000 records loaded |
| C2 | Send back | Code tries; no output exists; failures return nothing (lines 26–27) | One generated roadmap from a real run |
| C3 | Sifted out | Ranking is keyword counting (line 16), done before the model is called (line 19) | A ranking method the team can explain, compared with its current ranking |
| C4 | Sifted out | Vendor, customer-reported, select design partners, no baseline | Our own measured planning hours before and after |
| C5 | Send back | Only support is two conversations | Customer requests, tickets, or interviews asking for AI planning |
| C6 | Pass | First-hand account of two conversations; supports nothing beyond that | (n/a: it already says only what it says) |
| C7 | Sifted out | No competitor, product, or link | A named competitor and its launch page or release notes |
| C8 | Sifted out | Code contradicts "done" (lines 2, 5, 6, 10, 26–27) | Working build on real data with errors surfaced |
| C9 | Send back | Sponsor forecast, no estimate | Engineering estimate against a scoped list |
| C10 | Send back | Rests on C9 | C9's estimate fitting before Nov 14 |
| C11 | Sifted out | Ticket rows, emails, customer names leave the laptop (lines 21–24); key in source (line 5) | Security review; data minimized; credentials out of code |
| C12 | Send back | No test results; "it worked yesterday" (line 27) | Test output on a real export |
| C13 | Send back | No timing; 30 s is the timeout (line 24) | A timed run |
| C14 | Send back | No measure of PM time | Where PM hours go now; how many go to roadmap writing |
| C15 | Sifted out | Rests on C4 (sifted out) and C14 (missing); consequential for people | A measured time study, then a separate decision |

**Smallest evidence action:** before anything else, rotate the hard-coded key and stop sending ticket rows (with reporter emails and customer names) to the outside API until security has looked. Then fetch a real Jira export and one real output.
**Human decision:** _which claims go forward_ (recorded by the human, not the assistant). In this unattended run, all fifteen go to `bdk-sell-by` per the run instructions.
