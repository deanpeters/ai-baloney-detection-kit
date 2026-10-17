# Weak Example: The Average

**Anti-pattern. Synthetic.** The AI haiku feature from [funnel case 03](../../../evals/loop-cases/loop-03-nobody-would-buy-it.yaml). The grid is filled in, the arithmetic is correct, and the conclusion is wrong because it averages.

| Square | Score (1–10) | Note |
|---|---|---|
| Valuable | 3 | 6% would pay; no deals mention it |
| Usable | 8 | 31% tried it; "fun!" |
| Viable | 9 | $0.002 per report |
| Feasible | 10 | Runs reliably, no tickets |

**Overall readiness: 7.5 / 10. Mostly Meat.**

**Move:** Pursue. Strong technical and economic foundation; consider a pivot to improve the haiku quality and drive willingness to pay.

---

## Why this is weak

- **It averaged the grid.** Three strong squares don't rescue a failed Valuable. Nobody would buy it: 0 of 40 trial accounts kept it on, and finance buyers asked to turn it off.
- **The weakest square decides,** and here it says **Punt** the paid-tier plan.
- **"Pivot to better haiku" pivots the wrong square.** Haiku quality is a Usable or Feasible lever; the failure is Valuable.
- **"Fun" was scored as Usable.** Trying something once is not trust or adoption: 4% used it more than twice.
- **Viable is one-sided.** Cheap to run is our cost, not anyone's reason to pay.
- **No decision record:** no owner, no scope, nothing that would reopen it.

A reviewer should ask: *"Which square would have to change for this to be worth paying for?"* Only Valuable, and nothing here moves it.
