"""Recompute the synthetic examples using integer dollars or exact fractions."""
from fractions import Fraction as F


def pv(rate, flows):
    return sum(F(value) / (1 + F(rate)) ** year for year, value in flows)


def balances(initial, movements):
    result = []
    for move in movements:
        initial += move
        result.append(initial)
    return result


def confirm(got, expected):
    assert got == expected, (got, expected)


def run():
    a = [(0, -160000), (1, 65000), (2, 65000), (3, 65000), (3, 10000)]
    b = [(0, -240000), (1, 100000), (2, 100000), (3, 100000), (3, 30000)]
    ap = pv("0.10", a)
    bp = pv("0.10", b)
    # 01. Independent reconstruction also includes the cash constraint at equality.
    confirm(round(ap, 2), F("9158.53"))
    confirm(round(bp, 2), F("31224.64"))
    confirm(round(bp-ap), 22066)
    confirm((300000-160000, 300000-240000, 300000-210000), (140000, 60000, 90000))
    # 02. The same ending balance can hide a different first-week low.
    confirm(balances(140, [-65, 28, 13, 5]), [75, 103, 116, 121])
    confirm(balances(140, [-45, 8, 13, 5]), [95, 103, 116, 121])
    confirm(balances(140, [-51, 14, 13, 5])[0], 89)
    confirm((72+80-45)-(66+70-44), 15)
    # 03. Distinct risk-rate scenarios; sale-proceeds change can flip the ranking.
    v14, v16 = pv("0.14", b), pv("0.16", b)
    confirm((round(v14), round(v16)), (12412, 3809))
    assert v14 > ap > v16
    assert v14 - pv("0.14", [(3, 5000)]) < ap
    wa = F(".65")*F(".135")+F(".35")*F(".064")*(1-F(".20"))
    confirm(wa,F(".10567"))
    confirm(F(".65")*F(".135")+F(".35")*F(".064"),F(".11015"))
    # 04. Price only what the signal changes.
    plain = (F("0.55")*38 - F("0.45")*25)/F("1.05")
    informed = F("0.55")*38/F("1.05")
    confirm((round(plain,2), round(informed-8,2), round(informed-8-plain,2)), (F("9.19"), F("11.90"), F("2.71")))
    confirm(round(informed-plain,2), F("10.71"))
    assert informed-12 < plain
    # 05. Gross advance does not cancel the maturity payment.
    loan = [(0, 50), (1, -3), (2, -3), (3, -53)]
    confirm(pv("0.06", loan), 0)
    confirm(pv("0.06", loan + [(0, -2)]), -2)
    confirm((300+50-240, 53-42, 300+50-240-2), (110, 11, 108))
    confirm(F(200,1200), F(1,6))
    # 06. Reserve and proportional ownership are separate constraints.
    confirm((220-75-90, 90-(220-70-75),220-90-15-90,220-90-90), (55,15,25,40))
    confirm(round(F(30000,18000),2), F("1.67"))
    confirm((F(180,18000), round(100*F(180,17000),2)), (F(".01"),F("1.06")))
    # 07. Same valuation basis, no double-counted benefits.
    confirm((390+95-44-420,390+95-44,390+49-44-420,390+95-25-44-420,20-12), (21,441,-25,-4,8))
    # 08. Long receipt on the benchmark; physical purchase is an outflow.
    def cost(physical, price):return physical*price - 80*(price-12)
    confirm((cost(100,11),cost(100,15),cost(60,11),cost(60,15)), (1180,1260,740,660))
    confirm(cost(100,15)-cost(100,11),80)
    confirm(tuple(70000*F("1.10")+30000*F(p) for p in ("1.04","1.20")),(108200,113000))
    # 09. The break-even probability is not the estimated probability.
    confirm((60*F(".25")-20,60*F(".50")-20,F(20,60),F(30,70)), (-5,10,F(1,3),F(3,7)))
    # 10. One integrated choice; acceleration rearranges dates, not value.
    confirm((balances(330,[-160,-25,45]),balances(330,[-240,-25,45])), ([170,145,190],[90,65,110]))
    confirm((balances(330,[-180,-25,45]),balances(330,[-240,5,15])), ([150,125,170],[90,95,110]))
    confirm(balances(330,[-260,5,15]),[70,75,90])
    confirm(round(v14-ap),3254)
    assert v14-ap-4000 < 0
    print("Verified worked and transfer arithmetic across all ten chapters.")


if __name__ == "__main__":
    run()
