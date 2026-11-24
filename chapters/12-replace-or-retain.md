# Replace the Machine, Not the Budget Line

The old machine has not failed. It was inexpensive to buy, expensive to run, and valuable enough to sell. The technical team includes the old purchase price and excludes the lease income the site could earn. The resulting spreadsheet is detailed. Its question is wrong.

This lab distinguishes incremental cash from spending that appears in an equipment budget. Then it uses terminal cash flows to identify which side of the decision has borrowed an assumption about the future.

## State the counterfactual before listing cash flows

A distributor can retain an old system or buy a replacement. Each option serves the same required load. We already know the replacement's cash differences versus keeping the old system; these are incremental, not its complete operating statement. All values are thousands of dollars.

- A replacement costs 480 today.
- The distributor can sell the old unit today for 60 **net of any sale taxes** only if it replaces it. The old purchase price is irrecoverable and absent from the comparison. Its potential sale receipt is not.
- The replacement ties up 36 in incremental inventory today, all collectible as cash when it is removed from service at the end of year four. Assume no other working-capital movements.
- Operating cost savings before depreciation and taxes are 180 at each year-end for four years. Incremental depreciation versus keeping the old machine is 72 in each year. For this model use a 25% marginal cash-tax rate; all incremental deductions are usable in the same year. Do not assume this rate for an actual firm.
- A bay used by the replacement cannot be leased to a third party. Its foregone after-tax lease receipts would have been 15 at each of the same four year-ends and are not included in the 180. Assume the lease is a genuine otherwise-feasible choice.
- At removal in year four the replacement generates 70 in net-of-tax disposal proceeds and incurs 16 of after-tax closure costs, neither included in operations. The retained machine would have no corresponding disposal cash flow on that date.
- Use a common 9% annual rate under the stated case assumptions. Both alternatives terminate consistently at year four. No later operating cash is assumed.

**Attempt first.** Put each item on its date. Identify whether it belongs in the decision, and if so whether it is already tax-adjusted. Write the operating difference separately from the initial and final changes in inventory.

## Separate operating earnings from operating cash

The pre-tax profit improvement before the lease adjustment is 180 − 72 = 108. The incremental cash tax is 27. After-tax profit improvement is 81; adding back incremental depreciation of 72 gives 153 operating cash before the lease opportunity cost. Another path is 180 − 27 = 153. Subtract the already after-tax 15 exactly once, getting 138 in each year. Do not tax the 15 again or treat the 72 as cash paid a second time.

The order date costs 480 − 60 + 36 = 456. This is not the supplier's 480 invoice. It is the net change caused by the decision today. The sale gain or loss is not reconstructed from gross sale receipts: the problem already supplies net sale cash. An analyst who adds an extra assumed tax is not being conservative. They are changing the scenario.

At the end of year four there is 138 operating cash, 36 recovered inventory, 70 net salvage and 16 closure outflow, for 228. This leaves one model:

| Date | Initial and ongoing incremental cash ($000) |
| --- | ---: |
| Today | −456 |
| Year 1 | 138 |
| Year 2 | 138 |
| Year 3 | 138 |
| Year 4 | 228 |

Discounting these amounts gives about 54.84. Setting the inventory release to zero, without removing the initial need for it, would reduce NPV by the present value of 36 at year four. Omitting the entire inventory commitment has a different effect. In the original case inventory returns the same number of dollars as the investment, but it holds them for four years without a return. Cash recovery is not the same as zero cost.

## Catch the terminal assumption that moved the goalposts

The analyst who wrote the first report added a perpetuity of annual cost savings after closing the machine. The project has already sold the equipment and released the supplies needed to run. Those terminal proceeds and the later savings cannot coexist in this case. A successor system could be considered, but its reinvestment, risks and replacement dates would be modeled on both sides of the comparison.

As a separate valuation convention for an ongoing business, suppose sustainable year-five free cash flow is 52 and grows at 3% indefinitely; the applicable discount rate is 9%. Its value at year four under that stylized assumption is `52 / (0.09 − 0.03)`, or about 866.67. That value is not an extra receipt on the date the business shuts down. It prices the stream beginning in year five and requires a credible ongoing basis, including the reinvestment implied by the growth. The formula fails at growth equal to or above the rate for the assumed infinite stream; near equality its outputs become extremely sensitive. Never use it as a blank check because a spreadsheet accepts the denominator.

**Inspect the answer.** A simulated memo says, “Exclude foregone lease payments because they aren't an expense, and add 72 of depreciation to cash savings because it's noncash.” Explain why the lease payments are a relevant alternative and why the depreciation advice can overstate cash in a model that starts from cash savings instead of after-tax profit.

**Transfer A.** Half the forecast inventory recovery disappears and the closure payment increases from 16 to 29. Hold every other input unchanged. Rebuild the year-four line and recalculate NPV. Is a still-positive value enough to prove the decision is fundable on order day?

**Transfer B.** A manager asks you to accept an 8% perpetual growth rate for the separate ongoing-business illustration. Compare the arithmetic denominator at 3% and 8%, explain what would have to be true about reinvestment, and recommend an evidence request rather than automatically selecting the number that approves the project.

[Back to contents](../README.md)
