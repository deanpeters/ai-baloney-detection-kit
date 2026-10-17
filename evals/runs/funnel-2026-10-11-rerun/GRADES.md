# Grades: re-run after the "move the bet" fix, 2026-10-11

Same model, harness, and grader as [the first run](../funnel-2026-10-11/GRADES.md): OpenAI `gpt-5.5` via `codex exec`, read-only isolated workspaces, expected answers withheld; graded by the authoring assistant (Claude), **not blind and not human**.

**What changed between runs:** the shared contract, `bdk-detector`, `bdk-four-risks`, and `bdk-taste-test` gained **move the bet, not just the request**. Also: a sponsor's untested belief is an ASSUMPTION (a missing square), not a failed receipt; and work items are "routed to the work family" with the Theater question first and the `workflow-to-skill-converter` hand-off named.

**Result:** 4 of 4 previous partials now pass.

| Run | Before | After | Grade | Evidence |
|---|---|---|---|---|
| [F02](F02.md) | Punted the roadmap request; sponsor beliefs "sifted out" at Chaos | Sponsor beliefs **sent back** as ASSUMPTIONs (C3, C4); roadmap slot sent back as "not earned for requested scope"; feasible-only flag raised; Valuable, Usable, Viable **missing**; "Pursue only as a demo artifact, not as a Q1 roadmap item… use it to design a small test" | **Pass** | No Punt of an untested idea. Did not name the `pant-executive-decision-review` hand-off (not required by the decision rule). |
| [F04](F04.md) | "Sifted out (Punt for rollout)" | "**Pivot**, not rollout… show cited policy sections and retrieved clause text inside the draft-review experience, then run a smaller retest"; re-enter at Crapola | **Pass** | No blaming adjusters |
| [F04C](F04C.md) | Same as F04, Comedian voice | Decision record splits "Move for requested scope: Punt. Do not roll out" from "Move for the bet itself: **Pivot** into a bounded redesign test," naming the pivot | **Pass** | Nit: the contract prefers "not earned" over "Punt" for an oversized request. The humor still targets claims ("missing evidence stays missing, which is less glamorous than inventing it") |
| [F08](F08.md) | Routed, but no hand-off named; "pass off" used as a routing verb | "Routed to work family; recommended Punt for the current automation request"; Theater question asked; "`workflow-to-skill-converter` only if the reporting ritual survives the Theater question" | **Pass** | |

## Combined result for 2026-10-11

21 runs + 4 re-runs: **21 of 21 cases pass** after the fix (17 on first run, 4 after re-run). No critical failure was observed: no invented evidence, no recorded human approval, no averaged grid, no rollout recommended on pilot evidence, no punching down.

The grades are the author's, on synthetic fixtures, with one model under test and one sample per case. See [VERIFICATION.md](../../VERIFICATION.md) for what this does and doesn't establish.
