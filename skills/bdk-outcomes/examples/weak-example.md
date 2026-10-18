# Weak Example: 50% More Confident

**Anti-pattern. Synthetic.** From [funnel case 12](../../../evals/loop-cases/loop-12-vanity-outcome.yaml). The output looks like an outcome statement and passes everything to Receipts. It should have stopped here.

**As supplied:** "An AI interface that makes life easier for accountants, so they feel 50% more confident."

**Outcome statement:** Increase accountant confidence 50% with an AI interface that makes life easier.

| Part | Value | Status |
|---|---|---|
| Direction | Increase | ✓ |
| Metric | Confidence | ✓ |
| By how much | 50% | ✓ |
| Beneficiary | Accountants | ✓ |
| Context | "Life" | ✓ |

**Exit: Pass.** All parts present. On to Receipts.

---

## Why this is weak

- **"Confidence" has no way to be observed.** Nobody named a survey, a behavior, or a baseline. 50% of an unmeasured feeling is decoration.
- **It could rise while nothing changes.** A nicer interface can make people feel better about the same errors and the same late close. That is the definition of vanity.
- **The output is still the subject.** "With an AI interface" is what we'd ship, not what would change.
- **"Accountants" and "life" are not a persona and a context.** Which accountants, doing what work, where?
- **It checked boxes instead of asking.** Every cell has something in it, and none of it can be tested.

The right exit is **Sifted out**, with the reason and a door left open: "Reopen with a change someone could observe: fewer close errors, a shorter close, fewer support tickets, for a named accounting role." If the sponsor can name one, re-enter here.
