# Corporate Finance (AI Plus One)

**Status:** Expanded public draft 0.3

## About the book

Twenty chapters across the decision sequence and advanced laboratories. This is not an expert-edited textbook or a replacement for an existing edition.

An MBA-level book about making and defending choices with a firm's money. Readers are assumed to know basic financial statements and present value. Throughout the book you sit on the decision side of the table. You have to recommend an action, reconcile it with the cash the firm can use, and say what would cause you to reopen it.

Each chapter begins with a plausible decision and takes its logic apart. Record your first answer before reading the worked argument. The supplied wrong answers are deliberate teaching examples, not live tool outputs. All data are fictional. One optional use of AI is to ask it to challenge the reasoning after a first attempt; the independent calculation and the decision belong to the learner.

## Learning outcomes

- Value dated cash flows and distinguish an attractive investment from one the firm can afford to fund.
- Compare project risk, financing, payouts, acquisition choices, and hedges under explicit assumptions.
- Defend a board recommendation with checked calculations, alternatives, and triggers for reconsideration.

## Read the book

Start with [A Good Investment the Firm Cannot Yet Make](chapters/01-price-the-decision.md) or browse the [chapters folder](chapters/).

### Part 1 · Find the decision

1. [A Good Investment the Firm Cannot Yet Make](chapters/01-price-the-decision.md)
2. [Forecast the Bank Balance, Not the Month](chapters/02-dated-liquidity.md)
3. [The Rate Is a Claim About Risk](chapters/03-price-project-risk.md)
4. [Buy Information Before Buying Equipment](chapters/04-price-flexibility.md)

### Part 2 · Decide who pays, who gets paid, and when

5. [Finance an investment without disguising the cost](chapters/05-finance-the-investment.md)
6. [Return money without returning the safety margin](chapters/06-preserve-the-reserve.md)
7. [Buy a business without paying for your own work](chapters/07-price-the-acquisition.md)

### Part 3 · Keep a decision defensible after the vote

8. [Hedge the cash exposure you can name](chapters/08-hedge-a-named-exposure.md)
9. [Write the rule before seeing the answer](chapters/09-precommit-the-rule.md)
10. [Resolve the board's choices together](chapters/10-resolve-the-board-choices.md)

### Part 4 · Advanced finance laboratories

11. [Close the model before forecasting it](chapters/11-close-the-model.md)
12. [Replace the machine, not the budget line](chapters/12-replace-or-retain.md)
13. [Value the financing separately](chapters/13-value-the-financing-separately.md)
14. [Budget the portfolio, not the queue](chapters/14-budget-the-portfolio.md)
15. [Value the claim you can buy](chapters/15-value-the-claim-you-can-buy.md)
16. [Make the bid fit the calendar](chapters/16-make-the-bid-fit-the-calendar.md)
17. [Keep cash and rates in one currency](chapters/17-keep-cash-and-rates-in-one-currency.md)
18. [Read the covenant as a cash claim](chapters/18-read-the-covenant-as-a-cash-claim.md)
19. [Count the shares and the money](chapters/19-count-the-shares-and-the-money.md)
20. [Solve the adversarial board packet](chapters/20-solve-the-adversarial-board-packet.md)

## Resources

Use [the independent review problems](problems/independent-review.md) after your first complete pass. Every lab explicitly distinguishes its fictional assumptions from evidence needed for a real decision. Professional finance, legal, tax or accounting work requires its own facts and advice.

You can verify the examples offline using the [first case calculator](scripts/verify_case.py), [core example checks](scripts/verify_examples.py) and [advanced model checks](scripts/verify_advanced.py), all with Python 3’s standard library. The latter reads the [advanced synthetic inputs](data/advanced-cases.json). The checks test the modeled arithmetic, not the reasonableness of the assumptions or an expert's review.

Still pending in this draft: expert edit, bibliographic fact-check and a distinct course-ready teaching/assessment pass. The build depth varies by chapter.
