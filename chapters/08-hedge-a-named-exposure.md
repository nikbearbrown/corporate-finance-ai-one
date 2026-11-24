# Hedge the Cash Exposure You Can Name

The distributor has protected next year's input price. That's the headline. When it turns out to need fewer units than it hedged, the same contract gives it exposure in the opposite direction. The hedge has not broken; the forecast quantity changed. Before pricing anything, write the exposure as a unit, a date and a direction.

You will compute the combined effect of a purchase and a matched hedge in two states, then test what happens when the quantity does not match.

## Make the promise specific

Assume the distributor expects to purchase 100,000 units of a single packaging input at one future date. The hypothetical market price could be $11 or $15 per unit; these are scenarios, not current prices. It enters an illustrative financial settlement on 80,000 units at a fixed reference price of $12. At maturity the distributor receives `80,000 × (market price − 12)` if the number is positive and pays its absolute value if it is negative. It then buys all physical units at the market price. The time and benchmark price match perfectly, and there are no fees, credit losses or interim cash flows in this simplified contract. It is not an instruction to enter a real trade.

**Attempt first.** Work both price states. For each, multiply the physical quantity by the market price. Then subtract a positive settlement you receive or add a payment you make. Compare the gap between high and low cost with and without the hedge.

| Scenario | Purchase cost without hedge ($000) | Hedge receipt, negative = payment ($000) | Combined cost ($000) |
| --- | ---: | ---: | ---: |
| Price $11 | 1,100 | −80 | 1,180 |
| Price $15 | 1,500 | +240 | 1,260 |

The variation narrows from $400,000 to $80,000 in these two scenarios. It was not designed to make the company better off in both states; at $11 it pays more than it would without the contract. The protected 80,000 units effectively cost $12 each and 20,000 still cost the market price. These results do not measure all future risk.

## Read the conditions that were hidden in the numbers

The algebra held because the cash price and settlement reference matched. A real distributor's invoice may track a different grade, location or index. If the benchmark rises by $2 and the actual supplier price rises by $3, settlement on the benchmark cannot erase the whole increase. That difference is one form of basis risk. A separate problem is a temporary liquidity call on a contract with interim settlements; even when the final purchase is protected, cash may be required earlier. See the [CME glossary](https://www.cmegroup.com/education/glossary) for market terminology; the timing and matching assumptions above are defined by the example.

Now reduce actual purchases to 60,000 units without changing the contract. At a price of $11, physical cost is $660,000 and the firm pays $80,000 on the contract, for $740,000 total. At a price of $15, physical cost is $900,000 and the firm receives $240,000, for $660,000 total. Combined cost now falls when the market price rises. On this part of the outcome the firm is behaving like a holder of a long price position on 20,000 more units than it needs.

## Translate the contract, not merely the currency

A new packaging purchase is priced in euros and due at the end of six months. The company will owe €100,000 and pays suppliers from a dollar bank balance. Its two spot scenarios at the payment date are $1.04 and $1.20 per euro. Without any hedge, the dollar bill is $104,000 or $120,000.

Suppose a contract allows the firm to buy €70,000 for $1.10 per euro on exactly that date, guaranteed by construction of the example. Leave the remaining €30,000 unhedged. The dollar bill is $77,000 plus either $31,200 or $36,000. So it ranges from $108,200 to $113,000 in the specified cases. The favorable and unfavorable dollar outcomes got closer. The supplier still receives the same number of euros. The company took an exchange-rate exposure off one part of the purchase, not a supplier-quality or cost escalation risk off the entire transaction.

If the supplier changes the deadline, the assumed match is gone. If the distributor also has a valid euro receipt the same day, determine the net euro need before deciding the hedge quantity; do not count one receipt both as collateral and as cash available for the payment unless those rights genuinely coexist. Record dollars per euro, not euros per dollar. If the quote is inverted, divide rather than multiply; changing the quotation convention does not change the economics.

An operating group valuing a longer-lived foreign project faces a separate problem. Same-date translation of one bill does not tell you the right discount rate for a foreign stream. Forecast on one currency convention at a time, keep nominal rates with nominal modeled cash, and apply any conversion or repatriation assumptions on dated payment terms. A real tax or legal restriction belongs in the evidence before it belongs in the model.

**Inspect the answer.** A simulated risk report says an 80% hedge leaves exactly 20% residual risk. It forgot to specify 80% of which quantity, and exactly which risk. Write a correction that distinguishes notional matched units from the possible change in profit or cash.

**Transfer.** Suppose the supplier price includes a $0.80 premium to the settlement benchmark and it applies to all 100,000 units. Compute the increase in combined cost relative to the matched-price example for either state. Then list one piece of timing information before deciding whether the firm can afford the contract's temporary obligations.

[Back to contents](../README.md)
