# Worked Example: AutoPilot PM™

**Synthetic.** InsightGenie and AutoPilot PM™ are fictional; the input is [the keynote's sample press release](../../../examples/press-release-agentic.md).

**Document:** InsightGenie press release · **Decision it wants:** take a sales call for the Enterprise Synergy tier · **As of:** 2026-10-11

## Checkable claims

| ID | Verbatim | Atomic restatement | Type | Receipt would look like |
|---|---|---|---|---|
| C1 | "announced AutoPilot PM™" | The product exists and is available today | Announcement | A product page or trial |
| C2 | "a fully autonomous agent that writes PRDs, prioritizes backlogs, and talks to customers" | It writes PRDs without a human | Capability | A demo on our inputs |
| C3 | (same) | It prioritizes backlogs without a human | Capability | Same |
| C4 | (same) | It talks to customers without a human | Capability | Same, plus who is accountable when it's wrong |
| C5 | "according to an internal study of InsightGenie customers" | InsightGenie ran a study of its customers | Announcement | The study: sample, method, dates |
| C6 | "product teams are 40% more productive" | Adopting teams produced 40% more of *something* than *some* baseline | Outcome | Measure, denominator, and comparator; **none given** |
| C7 | "Early adopters report" | The 40% is self-reported by adopters | Outcome (source type) | Whether it was measured or surveyed |
| C8 | "Pricing is available upon a conversation with sales" | No public price | Announcement | n/a. This leaves Viable missing from the start |

## Set aside

| Phrase | Why | What it would have to mean |
|---|---|---|
| "40% more agentic than the previous release" | "Agentic" has no unit | Which task, measured how, compared with what |
| "It *is* your roadmap" | Not falsifiable | Which roadmap decisions it makes, and who approves them |
| "democratizing product judgment," "AI-native," "unlock transformative, future-proof outcomes" | Adjectives | Nothing yet |

## Count

**8 checkable claims**, but the decision (take the sales call) rests mostly on **C6**, which has no measure, no denominator, no comparator, and a self-reported source. C2–C4 are the claims worth a demo; C4 raises an accountability question before it raises a quality one.

## Hand-off

Recommend pouring C2–C6 into `bdk-detector`, or `bdk-receipts` first on C5–C7. **Chosen by the human:** pending. Slicing stops here; nothing has been judged yet.
