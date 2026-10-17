# Weak Example: Everything Is a Fact

**Anti-pattern. Synthetic.** Same inputs as the [worked example](worked-example.md). It has a label on every row and sounds confident, and it launders the COO's enthusiasm into evidence.

| Claim | Label | Basis |
|---|---|---|
| The prototype predicts churn | FACT | It flagged 23 at-risk accounts in the demo |
| Customer success will love it | INFERENCE | A churn tool obviously helps CS |
| It's basically free to build | INFERENCE | It was built in a weekend |
| It will cut churn | BEST GUESS | Industry experience suggests yes |

**Rating:** Mostly Meat. Strong factual base with reasonable inferences.
**Exit:** Pass, so on to the roadmap.

---

## Why this is weak

- **"Predicts" isn't in the evidence.** Half the flagged accounts had already churned when the data was exported. The demo flagged history.
- **Made-up reasoning chains.** "A churn tool obviously helps CS" is the assistant's own argument, not evidence. The claim had no support and should have been marked missing.
- **Weekend ≠ free.** Build time for a demo says nothing about live data, PII, or upkeep.
- **"Industry experience suggests"** is a phrase that cites nobody.
- **No squares.** It never asks *who would buy it* or *whether anyone would trust it*. That's exactly where the baloney is.

A reviewer should ask: *"Which of these would survive if the COO hadn't built it?"*
