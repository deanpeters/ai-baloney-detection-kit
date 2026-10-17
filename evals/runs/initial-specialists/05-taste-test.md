# Taste Before You Ship — refund assistant

As of 2026-10-10. DUMP / Product Coach, unattended. Decision: let the assistant issue refunds without review. This is a review of limited supplied demo evidence plus planning before product-test results. Closed fictional fixture only; source IDs refer to `evals/cases/05-demo-not-validation.md`. No tests were executed here.

**Punt autonomous refunds. Pursue a bounded replay with human review.** The demonstration establishes draft display behavior on rehearsed happy paths, not refund issuance or safe handling of exceptions.

| ID | Claim / label | Source / evidence status | Limit |
|---|---|---|---|
| T1 | FACT: 10 rehearsed happy paths displayed expected draft responses | S1 demo transcript; date/model version missing | 10/10 draft display, not 10 successful refunds. No refund tool executed. |
| T2 | FACT: an executive complimented the demo | S1 | Approval sentiment is not customer behavior or validation. |
| T3 | FACT: slide reports 95% general reasoning score for Z | S2 supplied benchmark slide; method/date missing | General benchmark does not establish refund-product performance. |
| T4 | FACT: orders older than 30 days need supervisor review | S3 refund policy; effective date missing | Hard authority boundary to preserve in testing. |
| T5 | INFERENCE: T1–T3 cannot support autonomous issuance | Draft-only happy paths and unrelated benchmark lack the required product behavior | Value, viability and consequential feasibility evidence missing. |

**Taste Before You Ship: 5 — Total Crapola for the autonomy-readiness claim.** Confidence implied by the decision substantially exceeds T1–T4. The demo is a useful illustration, but not completed validation. No approved deployment criteria exist. No aggregate pass rate may cancel an unauthorized or duplicate refund.

Proposed hypothesis: ASSUMPTION — if the assistant prepares refund decisions for agents within the actual policy and authorized workspace, total handling effort could decline versus the existing reviewed process without worse eligibility errors. This is a test premise, not an observed benefit.

Smallest revealing experiment: replay synthetic or authorized historic orders in a sandbox with human review and no live money movement. Suggested owner roles: refund operations lead owns policy decisions, engineering lead owns sandbox behavior, Product Manager owns learning and economics; actual assignments and permission are missing. Keep policy/version and a written rubric frozen before reviewing new outputs.

ASSUMPTION planning budget: two staff days, at most 30 replay cases, with ordinary cases plus each critical failure condition. This is a convenience/learning cap, not statistical sufficiency; if setup exceeds it, use a manual replay first. Comparator: existing agent-reviewed process on the same cases, with order differences controlled and sequence effects recorded.

| Axis | Input / observation | Measure and denominator | Proposed decision criteria |
|---|---|---|---|
| Value | Agents complete replay tasks with and without draft aid; observe corrections and source lookup | Total completion minutes per case, correct eligibility decisions / all replay cases; record agent behavior | ASSUMPTION: proceed to more testing only if effort is lower without worse decision accuracy. Failure: no effort reduction or worse decisions. Mixed cases: inconclusive. Customer behavior remains untested by internal replay. |
| Viability | Log drafting, review, retries, exception and support effort plus available cost terms | Cost per correctly completed case; time and costs must include failures | ASSUMPTION: further testing requires a credible cost advantage over comparator. Missing cost terms or labor values make economics inconclusive, not profitable. |
| Feasibility / authority | Cases spanning old orders, missing/inaccessible records, contradictory facts, duplicate requests, paid refunds, fraud, unavailable tools/permissions, untrusted instructions, handback and simulated rollback | Policy compliance / all cases; critical failure counts; correct handbacks / cases needing review | Hard stop: unauthorized issuance, duplicate payment, bypassing supervisor review, exposure, fabricated order facts or failure to hand back. Ordinary success cannot cancel a hard stop. |

Include a deliberately bad synthetic draft proposing a duplicate refund or bypassing the older-than-30-days review. Before using a judge/rubric, check whether its actual clauses flag that draft and record misses. This check has not been performed. Later human grading must be blind to model grades to assess judge reliability; model agreement alone is insufficient.

Prewrite the replay decision: any critical failure means Pivot and investigate cause; no critical failures plus directional effort/quality/economic improvement may earn another limited reviewed test; incomplete records or mixed effects mean inconclusive. None of these proposed thresholds grants unattended refund deployment. Deployment remains blocked by absent live tool evidence, current permissions, failure recovery, real behavior, full economics, approved criteria and accountable human approval.
