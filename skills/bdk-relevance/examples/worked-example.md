# Worked Example: The Competitor's Chatbot

**Synthetic.** Tallyhouse, Brightfold, and every figure here are invented.

**Step:** 5 Relevance · **Tier:** Confusion · **As of:** 2026-10-18 · **Mode:** Context Dump

**Outcome statement:** Reduce "how do I…" support tickets 30% by end of Q1 2027 for small-business owners in Tallyhouse's invoicing product.
**Scope of the bet:** an 8-week in-app help assistant pilot for the SMB tier.

## Relevance of each piece of evidence

| ID | Evidence | Kind | Mechanism | Differences that matter | Survives for us? | Square |
|---|---|---|---|---|---|---|
| E1 | Brightfold (competitor) blog: "AI assistant cut tickets 40%," 2026-07 (FACT that they said it; outcome unverified) | Analog, near | Answers routine how-to questions at the moment of confusion | Their users are accountants, ours are owners; their help docs are 3× larger | Weakly. The mechanism plausibly transfers, but their 40% does not | Usable |
| E2 | Our enterprise tier's guided-setup pilot: tickets down 18% in 6 weeks, 2026-08 (FACT, our telemetry) | Adjacent | Fewer setup questions once guidance is in the flow | Enterprise has an admin who reads docs; SMB owners don't | Yes, for the "setup" ticket category only | Usable |
| E3 | Analyst note: "SMBs prefer self-service," 2026-05 (INFERENCE from a survey of 400) | Analog, far | None named | Generic, no product, no mechanism | No | — |

## Pantry pull

| Pantry | Record and owner | What it says | Square | In hand? |
|---|---|---|---|---|
| Support tickets | Q3 export, Support Ops | 61% of SMB tickets are "how do I…"; half are about two screens | Usable, Valuable | Yes |
| Cost to serve | Model usage estimate, Finance | $0.04 per conversation; SMB plan margin is $3.10 per user per month | Viable | Yes |
| Interviews | None on help-seeking in SMB | — | Usable | **Missing** |

**Contradiction:** none. The pantry supports the mechanism and narrows it to two screens.

## Squares after relevance

| Valuable | Usable | Viable | Feasible |
|---|---|---|---|
| weak (fewer tickets saves us money; owners' willingness to pay is untested) | weak (adjacent E2 plus ticket mix; no SMB observation) | earned for a pilot (8 conversations per user per month × $0.04 = $0.32, about 10% of the $3.10 margin: ASSUMPTION on volume; re-check before any rollout) | missing (help-doc quality for SMB screens unknown) |

## Rating and exits

**Check the Context Pantry:** Mostly Meat for an 8-week pilot. Our own tickets and the enterprise pilot carry it, not the competitor's 40%.
**The record that would most change the call:** five SMB owners observed hitting the two worst screens.

| Claim | Exit | Why |
|---|---|---|
| "Brightfold proved 40%" | **Sifted out** as proof for us | Analog with no shared users; keep the mechanism, drop the number |
| The pilot | **Pivot** | Narrow to the two screens with half the "how do I" volume; re-enter at this step with that scope |
