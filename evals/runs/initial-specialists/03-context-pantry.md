# Check the Context Pantry — scheduling authority

As of 2026-10-10. DUMP / Product Coach, unattended. Decision: allow a Harbor Repair assistant to book and send appointments automatically. Closed fictional fixture; supplied evidence only. Source IDs refer to `evals/cases/03-context-conflict.md`.

**Pivot to investigating a draft-only helper.** Auto-send conflicts with the current policy and the dispatchers' stated workflow needs. The supplied context is sufficient to reject that change as currently proposed; it does not establish that a draft helper will improve outcomes.

| ID | Context / label | Source and status | Decision consequence |
|---|---|---|---|
| C1 | FACT: dispatchers report time lost gathering availability | S1 operations interview notes, 2026-10-01; reported experience | A coordination problem is present; its size and frequency are unmeasured. |
| C2 | FACT: dispatchers require approval because travel, access and emergencies invalidate slots | S1, 2026-10-01 | Calendar overlap alone does not establish a usable appointment. |
| C3 | FACT: only dispatchers may approve and send confirmations; assistants may draft | S2 policy effective 2026-09-01; no approved change supplied | Auto-send is outside current authority. |
| C4 | FACT: sponsor proposes removing dispatchers and auto-sending | S3, date missing | Direct conflict with C2 and C3; mandate does not settle the conflict. |
| C5 | INFERENCE: “just calendar matching” omits material workflow constraints | C2 plus sponsor's characterization in C4 | Removing review may add exceptions and rework; magnitude unknown. |
| C6 | BEST GUESS: draft preparation could address some gathering effort while preserving authority | C1 and permitted drafting in C3 | A testable alternative; benefit is not observed. |

Present: dispatcher user, availability-gathering problem, calendar coordination, material exceptions and approval boundary. Conflicting: sponsor's calendar-only definition and automatic-send goal versus operations and current policy. Missing: customer experience and requirements, current handling time, exception incidence and cost, schedule quality baseline, success criteria, integration reliability, economic model, support costs, and accountable policy-change owner. No auto-send pilot exists.

**Check the Context Pantry: 5 — Total Crapola for the auto-send proposal's use of context.** C2–C5 expose a consequential contradiction, rather than merely a thin brief. A useful policy receipt cannot rescue a proposal that disregards it. For a draft-only investigation, the context is sufficient to frame a small test, though important benefit and cost gaps remain.

The first dependency is authority: an accountable human must own any proposed policy change before auto-send can be reconsidered. Nobody is named; do not assume the sponsor holds that authority. Next, inspect actual dispatcher handling of travel, access and emergency cases. Suggested owner role: dispatch operations lead with policy owner; actual assignments and approval missing.

Smallest next action: observe a few scheduling tasks using the existing process, then compare calendar aggregation or deterministic availability filtering against a draft assistant with dispatcher approval. ASSUMPTION: a short internal observation is an acceptable planning scope, subject to authorized data access. Measure total dispatcher effort, valid confirmed slots, corrections and exception work; count review time as cost. Simplifying calendar gathering may help without generation. Customer benefit, feasibility and net economics remain unvalidated. Rating would improve when the proposal aligns with actual workflow and authority and its material gaps are made explicit; deployment needs separate validation.
