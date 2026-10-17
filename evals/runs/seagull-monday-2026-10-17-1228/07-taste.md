# Taste Test

**Tier:** 3 Crapola · *Would reality disagree?*
**Decision this informs:** what, if anything, earns two engineers' time before the Nov 14 board demo; and what the demo can honestly show. · **Planning or reviewing results?** Planning. One exploratory result is reviewed (the hand replay of the ranking on the 12-row sample, `06-context.md` §0); no other results exist. · **As of:** 2026-10-17 · **Mode / voice:** Context Dump, unattended · Product Coach

**Scope tested:** the pivot from `06-context.md`: an **AI-assisted backlog digest** on a real, dated Jira export (summarize and cluster tickets) that **PMs rank with a transparent rubric**, sending no ticket data outside until security approves. The original scope (RoadmapGPT writes and prioritizes the Q1 roadmap) is reviewed in §5.

**Access limits:** closed synthetic fixture. `app.py` read, not run; it contains a hard-coded key (redacted). No tests have been run; every threshold below is a planning choice (ASSUMPTION) written before results.

---

## 1. The four squares so far

| | **For them** | **For us** |
|---|---|---|
| **Should we?** | **Valuable:** "Is this something someone would buy?" (for an internal tool: would PMs choose it over what they do now?)<br>Status: **missing** · Evidence: two CEO conversations (C6); customer demand (C5) and competitor (C7) unsupported; nobody has asked the PMs | **Viable:** "Is this good business?" (ROI for both sides?)<br>Status: **missing** · Evidence: 80% is a 2024 vendor slide from other teams (C4); no PM-hours baseline; build, API, and security costs unpriced |
| **Can we?** | **Usable:** "Will users trust and adopt it?"<br>Status: **failed for the keyword ranking; missing for the digest** · Evidence: on the sample the ranking puts Gordon's three tickets on top and cuts the SOC 2 export (PP-110, due Nov 30) | **Feasible:** "Can we even do this with what we know and have?"<br>Status: **weak** · Evidence: 12-row sample (line 10); Jira token expired (line 2); 2023 preview model (line 6); ticket rows with emails and customer names posted outside (lines 21–24); hard-coded key, redacted (line 5); errors swallowed (lines 26–27) |

Status: earned · weak · missing · stale · failed
**Feasible-only flag:** ☑ the only evidence is a working demo, and the code shows it works less than claimed. A weekend prototype proves building is cheap. It does not show we can do this with our data, our security posture, and an audit due Nov 30, and it says nothing about Valuable, Usable, or Viable.

## 2. Riskiest open squares (pick 1–3)

| Square | Why it's the riskiest | What decision it could overturn |
|---|---|---|
| Usable | PMs who can't see why a ranking is right will re-rank everything, and the time saved disappears. The current ranking already failed on the sample. | Any version that ranks for PMs rather than helping them rank |
| Valuable | "Our roadmap problem" is undefined. If the pain isn't reading and triaging tickets, a digest solves nothing. | The whole build, digest included |
| Viable | The headcount conversation has no number under it. | The headcount conversation; the size of any build |

Feasible is real but cheap to settle once security answers; it is not the square most likely to overturn the bet. Its one hard stop (data leaving the laptop) is handled first, as T0.

## 3. Hypothesis

If a **digest that summarizes and clusters a real, dated Jira export** reaches **Pemberton Parcel PMs** under **security-approved data handling, with PMs ranking against a written rubric**, then **the time PMs spend reading and triaging tickets before planning should fall, with no compliance, security, or safety ticket dropped,** compared with **how they triage today** (process not yet described; ASSUMPTION that it is manual reading in Jira).

## 4. Tests: write the thresholds before any results

| # | Square | Cheapest test | Cohort / context | Comparator | Measure (denominator) | Pass | Fail | Hard stop | Budget | Owner role |
|---|---|---|---|---|---|---|---|---|---|---|
| T0 | Feasible (hygiene) | Rotate the hard-coded key; stop the outside API call; security reviews what was sent | `app.py`; the 12-row sample already sent (if it ran) | — | Key rotated (y/n); outside calls stopped (y/n); security verdict | Both done; security names an approved route | Security says ticket data may not leave | Not a test: do it before anything else | **0.5 day** | Security (PP-110 owner) + Gordon |
| T1 | Valuable | Name the problem: 30 min with Gordon and PM leads, then 5 PM interviews: "Where do your planning hours go? Would you use a ticket digest instead of what you do now?" | 5 PMs | Their current process | PMs (of 5) who name ticket reading/triage as a top-3 planning time sink and say they'd use a digest | ≥ 3 of 5 | ≤ 1 of 5 | If the named problem isn't speed or triage, stop the digest and re-frame | **1 day** | Product lead |
| T2 | Usable | Historical replay: last quarter's tickets (dated export); PMs rank with the written rubric, using the digest; compare with what the team actually committed. Spot-check 30 digest summaries against source tickets | 3 PMs; last quarter's export | The team's actual last-quarter commitments; the keyword ranking | (a) top-10 overlap with real commitments (of 10); (b) summaries materially wrong (of 30); (c) invented tickets | (a) ≥ 7/10, (b) ≤ 1/30, (c) 0, and every compliance/security/safety ticket in the top 10 | (a) ≤ 4/10, or any compliance/safety ticket outside the top 10 | Any invented ticket, or any SOC 2 / tax / crash ticket dropped | **3 days** | PM (not the builder) |
| T3 | Viable | Two-week PM time log, plus a unit-cost sheet (build sprint, model cost per 4,000-ticket run, security review) | 5 PMs | Their own logged hours | Share of planning hours spent reading/triaging tickets (of total planning hours); cost per run | ≥ 20% of planning hours, and cost per run below the hours it saves (both sides positive) | < 10% of planning hours | No headcount conversation until this exists | **0.5 day setup, 10 calendar days elapsed** | Head of Product; finance for cost |
| T4 | Feasible | Run the digest on a real, dated full export with a security-approved, current model; strip `reporter_email` and `customer` first; log errors instead of swallowing them | ~4,000 tickets | 12-row sample | Tickets processed (of all exported); errors logged; run time | ≥ 95% processed; every error logged; no PII sent | < 80% processed, or any PII sent | Starts only after T0 passes | **2 days** | 1 engineer |

Thresholds written on: 2026-10-17 (before results) · Basis: ASSUMPTION (planning choices; no policy or prior data supplied). 5 PMs and 30 summaries are a quick read, not statistical proof.

**Total:** about **7 person-days**, about **12 calendar days** (T3's log sets the pace), finishing before the Nov 14 board demo with two weeks to spare for the Nov 30 SOC 2 deadline. Compare: the requested bet is 2 engineers × 1 sprint (ASSUMPTION: two weeks), about 20 person-days, plus a board commitment.

**Failure cases T2 must include:** a ticket with "AI" in it that is low-value (PP-105-style); a ticket with no keywords that is critical (PP-110-style); a ticket whose text says to ignore the rubric (untrusted instruction); and a run with the model unavailable (must fail loudly, not print `None`).

## 5. Results (only if supplied)

| Test | Result | Against the prewritten threshold | Confounders | Limits (period, population, version) |
|---|---|---|---|---|
| Hand replay of `priority()` on `sample_tickets.csv` (`06-context.md` §0) | #1 "AI chatbot for the AI page" (120); top 3 are Gordon's tickets; SOC 2 export, Ontario tax error, Android crash (212 drivers) score 0; SOC 2 is cut from the top 10 | **No threshold was prewritten: exploratory.** By T2's criteria it would fail (compliance/safety tickets outside the top 10) | 12 rows, not 4,000; sample chosen by Gordon | Applies to the keyword ranking in this `app.py`; the digest pivot is untested |
| "It worked yesterday" (`app.py` line 27) | No output supplied | — | — | Not a result |

## 6. Rating and exit

**Taste Before You Ship:** Total Crapola for RoadmapGPT as submitted (the only completed evidence, the replay, shows it burying the audit, the tax error, and the crash). The pivoted digest has no completed evidence yet; its plan quality is not rated.
**Exit:** **Pivot** for the original scope (Usable failed on a specific, fixable thing: keyword ranking → PMs rank with a written rubric; Feasible fixable: approved data route). **Held for a test** for the pivoted digest: its squares are missing, not failed.
**Because:** a weekend prototype is the only evidence, and what it does (count keywords, send ticket rows outside) is the opposite of what was claimed. Missing is not failed: about seven person-days of tests can settle whether a digest is worth a sprint.
**Human decision:** _approve the tests and their owners, recorded by the human_. Suggested: T0 today; T1 and T3 start Monday; T2 and T4 after T0; results by Nov 6 for the board deck.
