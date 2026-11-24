# Keep Cash and Rates in One Currency

The international team values a project in euros, converts the answer to dollars, and recommends it. The home office translates every future payment at today's exchange rate and discounts at its dollar opportunity rate. It rejects the same project. Both models use correct arithmetic. One pairs cash flows with inconsistent rates.

This fictional example isolates the error with deterministic cash flows, a stylized pair of borrowing and lending curves, and no frictions. Do not infer that the case rates are available market quotes or that a risk-bearing foreign project can be priced using this exact shortcut.

## Choose a quotation convention and do not change it

Use dollars per euro throughout: today 1 euro is worth $1.10. The project pays 160 thousand euros today and receives 90 thousand euros at the end of each of the next two years. There are no taxes, conversion charges, terminal flows, restrictions or risks affecting the fixed receipts. The matched euro opportunity rate is 6% annually and the matched dollar rate is 9%, both compounded annually in this model. Funds can be borrowed and lent on those terms with either maturity.

At dates one and two, a contract to buy a euro for dollars is available at the price implied by the two rate curves and today's quote. To verify the direction, compare two ways of fixing one euro in (t) years. Buy (1/(1.06)^t) euros now and invest them for (t) years. This costs ($1.10/(1.06)^t) now. Alternatively pay for a dollar investment now and lock the currency exchange at (t). Consistency of the equivalent fixed flows in this no-friction example gives the future dollar-per-euro quote:

`F(t) = 1.10 × (1.09 / 1.06)^t`

It is about 1.13113 at year one and 1.16315 at year two. The quote is not a forecast of what an unhedged spot price will be. It is a contract price in the stipulated framework.

**Attempt first.** Work the valuation twice. On the euro road, keep all flows in euros until you obtain time-zero project value, then translate at today's exchange rate. On the dollar road, use the future exchange contracts for the cash receipts and the spot quote for today's cost. Discount the resulting dollar cash at 9%. Put the currency label on every line; an identical number with the wrong label is an error.

## Reconcile the roads

In euros the present value is −160 + 90/1.06 + 90/1.06², or 5.00534. At $1.10 per euro this is 5.50587 thousand dollars. In dollars the outlay immediately is 176. Future receipts fixed in dollars are about 101.8019 and 104.6831. Discount them at the stated dollar opportunity rate and subtract 176 to reach the same 5.50587. Algebra gives the same conclusion: `F(t)/(1.09)^t = 1.10/(1.06)^t` at each date.

If you translate the two future receipts at the time-zero spot and discount at the dollar rate, you get roughly −1.85 thousand dollars instead. Nothing in the case establishes that fixed stream of dollars; it is an incompatible valuation input. This is why checking only the final sign, or only the conversions, is not enough. A dated parity check can expose the mistake before an approvals meeting.

## Put the assumptions back

An uncertain, hard-to-hedge foreign project differs in several ways. Its cash flows may grow with local inflation, the borrower may pay credit spreads, the sales proceeds may not be repatriable on the stated date, and risk may covary with exchange movements. In that case separately document the currency of revenues, project costs and financing; the claims owners can actually receive; the timing of any restrictions and taxes; and how rate and cash conventions are linked. Do not substitute a hedging contract quote for a forecast of business demand or for a guarantee of counterparty performance.

**Inspect the answer.** An analyst divides the year-one euro receipt by the 1.13113 forward quote and calls the result dollars. Unit checking catches the error before arithmetic. Write out the units and cancel them. Then describe why a dollar-denominated loan still creates cash duties in dollars even if the parent values a subsidiary in euros.

**Transfer.** Keep every other assumption but make 10 of the year-two euro receipt inaccessible to owners until the end of year three. Assume no incremental fees, the same flat rate curves through year three and certainty of payout. Compute the euro PV change, then reconcile it from the dollar approach. Explain why a cash schedule may report a positive local bank balance before parent cash is available.

[Back to contents](../README.md)
