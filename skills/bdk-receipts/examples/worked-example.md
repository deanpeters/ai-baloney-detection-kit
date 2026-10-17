# Worked Example: Three Articles, One Origin

**Synthetic.** Brisket Labs, SpecPilot, and Copperline Software are invented. From [funnel case 01](../../../evals/loop-cases/loop-01-vendor-productivity-claim.yaml).

**Tier:** 1 Chaos · **Decision:** sign a 12-month, 60-seat SpecPilot contract by 2026-10-31? · **As of:** 2026-10-11 · **Mode:** Context Dump · **Access:** supplied excerpts only; no URLs opened.

## Claims

| ID | Claim | Announcement or outcome? |
|---|---|---|
| C1 | "SpecPilot boosts PM productivity 40%" | Outcome claim, repeated as fact |
| C2 | Brisket Labs ran an internal study showing faster spec drafting | Announcement (the release says so) |
| C3 | Copperline PMs find spec writing too slow | Outcome, first-party survey |

## Sources and origin groups

| Source | What it is | Traces to | Inspected? | Supports |
|---|---|---|---|---|
| S1 | Trade blog, 2026-09-02 | S3 | Excerpt only | That the blog repeated the figure |
| S2 | Newsletter, 2026-09-04 | S1 → S3 | Excerpt only | That the newsletter repeated it |
| S3 | Brisket Labs press release, 2026-08-28 | (origin) | Excerpt only | That the vendor *reports* 40% faster drafting, 12 internal users, no method |
| S5 | Copperline PM survey, 2026-09-20 | (origin) | Supplied | 9 of 14 PMs say specs take "too long"; median self-reported 5 h |

**Origin groups:** {S1, S2, S3} → **one origin**, the vendor's own unpublished study. {S5} → one first-party origin.

## What survived

- C2 is a FACT about the release, not about anyone's productivity. The vendor measured *drafting speed*, not *productivity*; the word changed on the way through S1 and S2.
- 12 internal users, no baseline, no method, and an obvious incentive: weak authority for a 60-seat annual decision.
- C3 is a solid first-party receipt for **Valuable** (there is pain) but not for this tool.

## Squares informed

Valuable: weak (pain is real; no evidence this tool relieves it). Usable: missing. Viable: missing (price known, ROI unmeasured). Feasible: weak, vendor data only.

## Rating and exits

**Show Me the Receipts: Mystery Meat** for C1. One interested origin with no method cannot be weighed.

| Claim | Exit | Reason |
|---|---|---|
| C1 "40% productivity" | **Sifted out** | One vendor origin, no method, and the claim outgrew what the origin measured |
| C2 vendor study exists | **Send back** | Ask Brisket Labs for the study method and raw counts before any pilot |
| C3 Copperline pain | **Pass** | First-party, current; carry to the Confusion tier |

**Smallest evidence action:** request the study's method from the vendor and run `bdk-sell-by` on the benchmark's model version.
**Human decision:** pending. The assistant recommends; the PM lead decides what goes forward.
