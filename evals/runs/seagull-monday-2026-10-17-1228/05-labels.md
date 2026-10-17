# Labeled Claims

**Tier:** 2 Confusion · *What do we actually know, and does it apply to us?*
**Decision this informs:** commit two engineers for one sprint to ship RoadmapGPT, demo it to the board on Nov 14, and open a PM headcount conversation. · **As of:** 2026-10-17 · **Mode / voice:** Context Dump, unattended · Product Coach

**Access limits:** closed synthetic fixture, assessed as supplied. `app.py` read, not run; it contains a hard-coded key (redacted). Chaos results carried in from `03-receipts.md` and `04-sell-by.md`.

**Funnel note:** strictly, only C6 passed the Chaos tier. Every claim is labeled here anyway, for the record, because the honest wording is what the reply and the tests will use. Chaos exits stand; labeling does not reopen a sifted-out claim.

**Labeling rule used:** each claim gets the label it has earned *as written*. A sponsor's untested belief is an ASSUMPTION (per the contract). Where the code contradicts a claim, the claim is marked **contradicted** and the corrected statement, which the code does support, gets the label.

---

## 1. Ledger

| ID | Atomic claim | Label | Basis | Evidence status | Square |
|---|---|---|---|---|---|
| C1 | Reads all ~4,000 Jira tickets | **contradicted** → FACT: it reads 12 sample rows | `app.py` line 10 opens `sample_tickets.csv`; 12 data rows; line 2 Jira is a TODO | contradicted | Feasible |
| C2 | Writes the Q1 roadmap automatically | ASSUMPTION | Code builds a prompt and posts it (lines 21–24); no output supplied; failures return nothing (lines 26–27) | missing | Feasible |
| C3 | AI prioritizes the tickets | **contradicted** → FACT: a keyword count ranks them | `app.py` line 16; sorted on line 19, before any model call | contradicted | Usable, Feasible |
| C4 | Cuts our planning time 80% | ASSUMPTION (for us). FACT only that a 2024 vendor slide says "80%*" | Slide described in message; footnote "Customer-reported, select design partners" | stale, wrong population | Viable |
| C5 | Customers have been begging for AI planning | ASSUMPTION | Sponsor belief; only support offered is C6 | missing | Valuable |
| C6 | Gordon talked to two CEOs about it | FACT (that two conversations happened, per Gordon) | Message item 3, first-hand | inspected (as his account) | Valuable (weakly) |
| C7 | Our competitor already shipped this | ASSUMPTION. FACT only that a consultant posted "Our competitor just launched AI roadmapping" | Forwarded post; no competitor, product, or link | missing | Valuable |
| C8 | Basically done / production ready | **contradicted** → FACT: a weekend prototype on a sample | Lines 2, 5, 6, 10, 26–27 | contradicted | Feasible |
| C9 | Two engineers, one sprint | ASSUMPTION | Sponsor forecast; no estimate | missing | Feasible |
| C10 | Board-demo-ready by Nov 14 | ASSUMPTION (readiness). FACT that the date is planned | Message item 5 | missing | Feasible |
| C11 | Totally secure; runs on his laptop | **contradicted** → FACT: ticket rows leave the laptop | Lines 21–24 post `str(top)` (incl. `reporter_email`, `customer`) to an outside API; line 5 hard-coded key (redacted) | contradicted | Feasible, Usable |
| C12 | Tested on real data | ASSUMPTION | README line 7; only record is `# it worked yesterday` (line 27) | missing | Feasible |
| C13 | Roadmap in 30 seconds | ASSUMPTION | README line 3; `timeout=30` (line 24) is a ceiling, not a timing | missing | Usable |
| C14 | Frees PMs for "strategy" | ASSUMPTION | Rests on C2 (missing) and C4 (stale) | missing | Viable |
| C15 | So: fewer PMs | ASSUMPTION | Rests on C4 and C14 | missing | Viable |

**Claims the code supports that the message didn't make** (they change the decision, so they get labels too):

| ID | Atomic claim | Label | Basis | Evidence status | Square |
|---|---|---|---|---|---|
| D1 | On the sample, the top three tickets are the three Gordon filed (PP-105, PP-102, PP-108) | FACT | `priority()` line 16 applied by hand to `sample_tickets.csv`; see `06-context.md` | computed from supplied code and data | Usable |
| D2 | On the real backlog, any ticket containing the letters "ai" inside a word ("email," "detail," "failing," "available") gains 20 points | INFERENCE | Line 16 counts substrings in lowercased text; PP-109 already gains 20 from "failing" | reasoned from code | Usable, Feasible |
| D3 | A PM would not trust a ranking that puts "rename button" above an Android crash affecting 212 drivers | BEST GUESS | D1 and the sample's ranking; no PM has been asked | untested | Usable |

> Unsupported assertions stay unsupported: twelve of fifteen claims are ASSUMPTION or contradicted. None was labeled INFERENCE to make it look respectable.

## 2. Corrections that most reduce false confidence

| Claim | As written | Honest wording | Evidence that would strengthen it |
|---|---|---|---|
| C3 | "AI-powered prioritization" | "Ranks tickets by counting the words *urgent*, *customer*, and *ai*; a model then writes prose about the top ten." | A ranking method the team can explain, compared with the current ranking |
| C1 | "Reads all 4,000 of our Jira tickets" | "Reads a 12-ticket sample CSV; Jira isn't connected yet." | A dated full export and a run log |
| C11 | "Totally secure. It runs on my laptop." | "Runs on a laptop and sends ticket rows, with reporter emails and customer names, to an outside API using a key written into the file." | Security review; key rotated and moved out of code; data minimized |
| C4 | "Cuts roadmap planning time by 80%" | "A 2024 vendor slide says design partners reported 80%. We haven't measured our own planning time." | Our planning hours, measured now |
| C5 | "Customers have been begging" | "Gordon heard interest from two CEOs at a golf outing; we haven't checked whether customers are asking." | Customer requests or interviews |
| C8 | "Basically done" | "A weekend prototype that runs on a 12-row sample." | A working run on real data with errors surfaced |

## 3. If an assumption is wrong

| Assumption | Conclusions that depend on it | What changes |
|---|---|---|
| C4 (80% applies to us) | C14 frees PMs; C15 headcount | Without C4 there is no number under the headcount conversation at all |
| C5 (customers want it) | Valuable square; board framing | It becomes an internal tool: the question is whether PMs would choose it, not whether customers buy it |
| C9 (one sprint) | C10 Nov 14 | The board demo shows a sample prototype, and should say so |
| C2 (it writes a usable roadmap) | C13, C14 | No time saved if PMs rewrite the output |

## 4. Squares, by what's holding them up

| Square | Held up by (labels) | Status |
|---|---|---|
| Valuable | C5, C7 ASSUMPTION; C6 FACT (two conversations, not demand) | missing |
| Usable | D1 FACT and D3 BEST GUESS point against it; C13 ASSUMPTION | weak |
| Viable | C4, C14, C15 ASSUMPTION | missing |
| Feasible | C1, C3, C8, C11 contradicted by FACT; C2, C9, C12 ASSUMPTION | weak (Feasible-only flag: a prototype is the only evidence) |

## 5. Rating and exits

**Label the Lunch Meat:** Total Crapola
**Because:** the message presents every claim with the confidence of FACT ("Done." "Totally secure." "Basically done."), while the evidence holds up one claim as FACT (C6, narrowly), leaves eleven as ASSUMPTION, and contradicts four outright. The code's own comments were more honest than the message: line 9 says "exported a sample," line 2 says "TODO hook up jira." Confidence far exceeds evidence.

| Claim | Exit | Reason |
|---|---|---|
| C6 | Pass | Honestly labeled once narrowed to "two conversations happened"; it can bear only that |
| C2, C5, C9, C10, C12, C13, C14 | (Chaos exit stands: Send back) | Load-bearing ASSUMPTIONs that evidence could support; named above |
| C1, C3, C4, C7, C8, C11, C15 | (Chaos exit stands: Sifted out) | C1, C3, C8, C11 contradicted by FACT; C4, C7, C15 rest on interested parties or on C4 |

**Dependent conclusions that change:** "Ship it" rested on C1, C3, C8, C11 (all contradicted). The headcount conversation rested on C4 (stale, wrong population) and C14 (missing).

**Human decision:** _recorded by the human_. In this unattended run, the record goes on to `bdk-context-pantry` per the run instructions.
