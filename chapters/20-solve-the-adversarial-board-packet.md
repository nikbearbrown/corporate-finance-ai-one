# Solve the Adversarial Board Packet

The board has a ranked project list, a term sheet and a revised collections forecast. One ranking uses an unavailable funding plan. One forecast assumes the collections change is already signed. One memo prices a fee twice. Your job is to identify the smallest decision the company can honestly approve and the first item that would justify changing it.

This capstone is distinct from the short exercise in Chapter 10. It combines a matched-risk valuation, a nominal-dollar payment ledger, the separation of financing value from asset value, and a decision trigger. The case is fictional. All cash amounts are thousands of dollars and ordinary positive numbers denote amounts, not signed cash flows, unless labeled.

## Packet A: what the assets do

Choose between an internal line expansion and a route purchase. They serve the same strategic expansion and are mutually exclusive. Under the stated model, both start now, have three years of operating cash and end with a terminal sale. Use the risk-matched rate supplied separately for each: do not assume contractual loan pricing should replace it.

| Item | Internal line | Route purchase |
| --- | ---: | ---: |
| Investment today | 320 | 385 |
| Annual after-tax operating cash, at each year-end | 130 | 165 |
| Extra after-tax sale cash, end of year 3 | 25 | 30 |
| Required operating return | 10% | 13% |

These cash flows are incremental and exclude payments to financing claimants. There is no bridge to a continuing value: both assets terminate. If you discard the final proceeds to make one investment look less speculative, mark that as a separate scenario rather than silently changing the proposal.

## Packet B: the actual wallet and loan terms

There is 500 of unrestricted cash immediately before investing. The board requires 130 remaining immediately after investment, at the end of week one and at the end of week two. Firm-level net cash apart from the order and any financing or fee is −50 in week one and +35 in week two. These figures apply equally to both alternatives and are **not** added to their valuation streams. Ordinary debt and future commitments outside these dates are not supplied; do not promise broader liquidity.

The lender will commit a loan of 55 for the route purchase only. The proceeds would be unrestricted at signing. It charges a 4 arrangement fee immediately and pays the remaining net amount to the buyer. The firm would pay 8% annual interest each year and repay principal at the end of year three. Use 8% to value the stipulated contractual loan flows as equivalent to the advance before the fee. Ignore cash-tax effects and other financing benefits or costs, except the shown fee. These assumptions do not establish availability of the loan to the internal alternative or feasibility in every later period.

A customer may accelerate 20 of receipts from week two into week one without any change in amount or additional cost. A signed acceptance reaching treasury before the vote is required under the scenario; an unconfirmed email does not count. Treat the shift as a liquidity change. There is no separate incremental valuation benefit attributed to accelerating the firm's baseline cash in this case. Keep those assumptions visible; a real value analysis might measure other costs or time value.

## First attempt

1. Calculate investment values on the supplied cash and rates. Derive the contractual loan payments and their PV at the stipulated matching yield before the fee. State the net modeled financing adjustment without hiding it in the operating discount rate.
2. Make an order/week-one/week-two cash table for the internal option, the route with no loan, the route with the committed loan, and the route with both loan and confirmed acceleration. For each, state the first date the constraint fails, if any.
3. Write a one-sentence recommendation before and after the signed customer acceleration arrives. If your action changes, show the cause. If it does not, explain why a newly feasible choice can still be inferior.
4. Independently vary one assumption, and document the capacity, value, and evidence that would be needed to move your recommendation. Do not ask an AI tool to choose before you've recorded your own answers.

## Worked teardown

Unfunded operating NPV is about 22.07 for the internal line and 25.38 for the route purchase. In this calculation route has a gross edge of about 3.31. At the stipulated yield, the 55 loan advance is offset in present-value terms by 4.4 annual interest for three years and 55 principal in the last year. The financing contribution therefore nets to −4 after the fee. A funded route has modeled APV 21.38 before any other effects, below internal's 22.07. The advance matters for availability but does not add 55 of value.

| Choice | Immediately ($000) | Week 1 ($000) | Week 2 ($000) | Clears all supplied dates? |
| --- | ---: | ---: | ---: | --- |
| Internal | 180 | 130 | 165 | Yes, exactly on limit in week 1 |
| Route, no loan | 115 | 65 | 100 | No, immediately |
| Route, loan incl. fee | 166 | 116 | 151 | No, week 1 |
| Route, loan and confirmed acceleration | 166 | 136 | 151 | Yes |

A model then tries to lower the route's NPV another 4 because the ledger shows cash being paid for the fee. It has confused two calculations. Show the single fee once when calculating net modeled financing value and once when tracking the relevant dated cash balance. Do not subtract it twice from economic value, and do not omit it from the cash forecast merely because it appeared in the valuation schedule.

The model supports choosing internal in both states given the stated weights and rules. It just meets the weekly floor, which is a decision to demand better collection evidence before committing, not a reason to invent a larger margin. A fee below the unrounded 3.308… advantage in this simplified comparison would remove the route's current valuation disadvantage, but only an actual agreement, verified liquidity and recomputed case could make a changed proposal actionable. A fee equal to the unrounded advantage makes the measures tie, not a victory.

## Defend the decision once the data move

The controller reclassifies 20 of opening cash as held for a restricted purpose. The safe starting balance was 480, not 500. Recompute the internal plan and the funded accelerated route. Name the first failing date and the minimum verified amount of additional opening cash that would close the tightest supplied gap for each. An action can be rejected or deferred even when no alternative clears the current test; do not select one by NPV alone. New funds may carry a cost and further obligations.

A second analyst runs the right calculator but asks an AI tool to summarize only the table showing the route can pass cash. Have a peer or a model challenge your decision using **one** of four questions: which funding path was actually committed, which cash time is binding, which risk rate prices the operating cash, or which fee already belongs in APV? Verify the response against the specified packet rather than asking for another opinion. If agreement persists for a different reason than your own, keep both rationales and explain whether the distinction changes the action.

Your final one-page deliverable has five parts: the action with date and authority, a clean baseline, a labeled adverse case, a numeric decision trigger with its evidence, and one unanswered question outside these dates. It should let a skeptical director reproduce the recommendation without a copy of the chat transcript.

[Back to contents](../README.md)
