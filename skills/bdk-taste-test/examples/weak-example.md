# Weak Example: The Demo Passed

**Anti-pattern. Synthetic.** Same inputs as the [worked example](worked-example.md). It has a results table, a percentage, and a confident call, and it tests the wrong square and blames the people.

## Results

| Metric | Result | Target | Status |
|---|---|---|---|
| Accuracy | 94% | 90% | ✅ Pass |
| Drafts generated | 1,240 | 1,000 | ✅ Pass |
| Uptime | 99.9% | 99% | ✅ Pass |

**Adoption note:** some adjusters are resisting the new tool and rewriting drafts unnecessarily. Recommend change management training and a usage mandate.

**Rating:** Mostly Meat. **Exit:** Pass. Roll out to all 120 adjusters.

---

## Why this is weak

- **It tested the easy square.** Accuracy, volume, and uptime are Feasible. Usable ("Will users trust and adopt it?") was never measured, though the pilot log answers it: 70% rewritten, 2 minutes slower.
- **Targets appeared with the results.** Nothing shows 90% was set in advance.
- **Outputs, not outcomes.** "1,240 drafts generated" is activity. The backlog is the outcome.
- **It punches down.** Calling careful adjusters "resistant" turns a product finding into a people problem. They can't see which clause the draft used, so they check everything. That is correct behavior.
- **No hypothesis, no hard stop.** There's no "then we will" tied to the backlog, and nothing that must never happen. A test that can't fail can't teach.
- **A mandate is not adoption.** Forcing use of a tool that makes the job slower makes Viable worse.

A reviewer should ask: *"Which of these numbers would change if nobody trusted the output?"* None of them would.
