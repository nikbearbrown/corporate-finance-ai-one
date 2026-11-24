# Budget the Portfolio, Not the Queue

The committee has four good projects and enough cash to undertake two. Its analysts rank them by value created per dollar. That sounds efficient. Then management discovers that the scarce input might not be a dollar. It might be a day of commissioning capacity or the only pay window the firm can afford.

You will compare complete feasible bundles and estimate the value of relaxing a binding resource. These proposals are fictional; expected NPV calculations have already been supplied at the appropriate rate for each project. Projects are indivisible, cash spending falls on the same date, and project values add because the finance team found no overlaps except for the listed resource constraints. If those conditions fail, the ranking must be rebuilt.

## Write the constraints before ranking

The available initial investment budget is 150 thousand dollars. The commissioning lead can provide 11 person-days during the critical window; every project must be commissioned in that window. Projects can run simultaneously only when both totals fit. Unspent budget and days have zero modeled incremental value in this static exercise. Doing nothing is allowed.

| Project | Date-zero investment ($000) | Commissioning effort (person-days) | NPV ($000) |
| --- | ---: | ---: | ---: |
| A | 90 | 6 | 42 |
| B | 60 | 6 | 27 |
| C | 70 | 4 | 34 |
| D | 45 | 3 | 22 |

**Attempt first.** Rank projects by NPV, then by NPV divided by investment. Do not confuse the latter with total discounted inflows divided by the initial outlay; for a normal single initial outlay, adding one to each NPV-per-invested-dollar statistic gives the analogous profitability index for these examples. Instead of choosing a preferred ordering, enumerate all feasible bundles.

| Pair | Cash ($000) | Days | NPV ($000) | Feasible? |
| --- | ---: | ---: | ---: | --- |
| A + B | 150 | 12 | 69 | No: days |
| A + C | 160 | 10 | 76 | No: cash |
| A + D | 135 | 9 | 64 | Yes |
| B + C | 130 | 10 | 61 | Yes |
| B + D | 105 | 9 | 49 | Yes |
| C + D | 115 | 7 | 56 | Yes |

The least expensive triple costs 175, so all triples violate cash. None of the single projects is better than the best feasible pair. The selected bundle is A + D, with 64 NPV. A mechanical value-per-dollar ordering would take D first and C next, leaving too little cash to add another and producing only 56. This is not a flaw in division. An indivisible combination is not the same problem as buying fractional units from a continuous supply.

## Price the resource only in the actual decision

Buying one extra available day at time zero makes A + B feasible; it produces 69 before paying for the day. At unchanged base investment budget, the gross value gain is 5. If the fee is paid from a separate unrestricted overhead budget and everything else stays unchanged, 5 is the break-even fee. If it must come from the same 150, any positive fee makes A + B too expensive unless another source or concession is identified. The statement “capacity is worth 5” is conditional on how the capacity is purchased and paid for.

The same caution applies if the base budget changes. With 10 additional investment dollars and capacity unchanged, A + C now fits at 160 with 10 days for 76 before the cost of extra funds. The project pair changes again. These are discrete changes, not a smooth return for every extra dollar. A portfolio model built on continuous approximations may be useful if it can prove its constraints fit the decision, not because it prints more digits.

## Test the assumption that projects add

Suppose A and D both rely on conversion of the same distributor customer. Their standalone NPVs include the full benefit separately. The teams agree that undertaking both together would reduce their nominal combined NPV by 8. The pair is still feasible in cash and days but now returns 56, below B + C at 61. The constraint did not change; the value of the combination did.

**Inspect the answer.** A prepared model returns A + C without checking cash. A second model returns C + D and mentions both constraints but does not examine alternatives. These are different failures: one chose a prohibited outcome; the other chose a permitted but inferior outcome. Require the record to show both feasibility and dominance.

**Transfer.** Keep the 150 and 11 limits but require the choice to include at least one of B or C for compliance testing. Apart from this extra condition use the original values and additive assumption. Determine the best bundle and opportunity cost relative to the unconstrained-by-compliance solution. Then state what evidence would allow the team to avoid treating a “must” requirement as just a small cost penalty.

[Back to contents](../README.md)
