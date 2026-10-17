# Weak Example: The 90-Day Rule

**Anti-pattern. Synthetic.** Same inputs as the [worked example](worked-example.md). It looks rigorous because it applies a rule consistently. The rule is the problem.

## Ledger

| Evidence | Age | Status |
|---|---|---|
| April pilot results | 180 days | ❌ Expired (> 90 days) |
| April decision record | 180 days | ❌ Expired |
| Provider price sheet | 26 days | ✅ Fresh |
| FAQ policy revision | 40 days | ✅ Fresh |

**Rating:** Total Crapola. Most evidence is past the 90-day sell-by date.

**Exit:** Sifted out. Punt the assistant; the evidence is too old to trust.

---

## Why this is weak

- **An invented expiry window.** Nothing supports 90 days. Freshness depends on what changed, not on a calendar.
- **It never read the triggers.** The decision record named exactly what to re-check; the weak version ignored them and missed that the model is being retired.
- **Fresh is not the same as reassuring.** The price sheet is fresh *and* says cost rose 40%. "✅ Fresh" hides the finding.
- **Stale became false.** Old evidence was treated as disproof, and a working assistant got punted instead of re-tested.
- **Durable evidence was thrown out.** The analysts' lookup pain hasn't changed.

The right exit is **Send back**: refresh Feasible and Viable, keep the rest dated.
