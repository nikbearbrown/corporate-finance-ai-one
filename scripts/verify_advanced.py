"""Verify the published fictional advanced labs with exact rational arithmetic."""
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "advanced-cases.json"


def value(rate, flows):
    return sum(Q(cash) / (1 + Q(rate)) ** year for year, cash in flows)


def balances(initial, *events):
    result = []
    for cash in events:
        initial += cash
        result.append(initial)
    return tuple(result)


def run(data):
    expected_checks = 0

    def same(actual, expected):
        nonlocal expected_checks
        if actual != expected:
            raise ValueError(f"check {expected_checks + 1}: {actual!r} != {expected!r}")
        expected_checks += 1

    def rounded(actual, expected, precision=2):
        same(round(actual, precision), Q(expected))

    # 11. Close the income, cash and accounting bridges.
    a = data["accounting"]
    o, p, c = a["opening"], a["period"], a["closing_non_cash"]
    opening_assets = sum(o[k] for k in ("cash", "ar", "inventory", "ppe"))
    same(opening_assets, o["ap"] + o["debt"] + o["equity"])
    inc = p["sales"] - sum(p[k] for k in ("cogs", "salaries", "depreciation", "interest", "tax"))
    collect = p["sales"] + o["ar"] - c["ar"]
    purchase = p["cogs"] + c["inventory"] - o["inventory"]
    pay_suppliers = o["ap"] + purchase - c["ap"]
    direct = collect - pay_suppliers - p["salaries"] - p["interest"] - p["tax"]
    indirect = inc + p["depreciation"] - (c["ar"] - o["ar"]) - (c["inventory"] - o["inventory"]) + (c["ap"] - o["ap"])
    cash = o["cash"] + direct - p["capex"] + p["borrowing"] - p["distribution"]
    closing_ppe = o["ppe"] + p["capex"] - p["depreciation"]
    closing_debt = o["debt"] + p["borrowing"]
    closing_equity = o["equity"] + inc - p["distribution"]
    same((inc, collect, purchase, pay_suppliers, direct, indirect, cash), (50, 328, 225, 220, 24, 24, 164))
    same(cash + c["ar"] + c["inventory"] + closing_ppe, c["ap"] + closing_debt + closing_equity)
    same((cash-12, c["ar"]+12, direct-12), (152,124,12))
    same((cash+9, c["ap"]+9, direct+9, direct+20, p["borrowing"]-p["distribution"]-20), (173,74,33,44,-15))

    # 12. Independent cash and earnings derivations, with a broken recovery case.
    a = data["replacement"]
    op_tax = (a["savings"] - a["depreciation"]) * Q(a["tax"])
    ann = a["savings"] - op_tax - a["foregone_rent"]
    same(ann, (a["savings"] - a["depreciation"])*(1-Q(a["tax"])) + a["depreciation"] - a["foregone_rent"])
    order = -a["unit_cost"] + a["old_sale"] - a["working_capital"]
    terminal = ann + a["working_capital"] + a["new_sale"] - a["closure"]
    same((order,ann,terminal),(-456,138,228))
    stream = [(0,order),(1,ann),(2,ann),(3,ann),(4,terminal)]
    rounded(value(a["rate"], stream), "54.84")
    broken = stream[:-1] + [(4, terminal-18-13)]
    rounded(value(a["rate"], broken), "32.88")
    rounded(Q(52)/(Q(".09")-Q(".03")), "866.67")
    same(Q(52)/(Q(".09")-Q(".08")), 5200)

    # 13. Asset cash, tax benefit, and maturity schedule must not overlap.
    a = data["apv"]
    rate, yield_, tax = [Q(a[k]) for k in ("operating_rate","debt_yield","tax")]
    debt = a["borrowed"]
    coupon = yield_ * debt
    same(value(yield_, [(0,debt)]+[(t,-coupon) for t in range(1,5)]+[(4,-debt)]), 0)
    shield_schedule = [(t,coupon*tax) for t in range(1,5)]
    unlevered = value(rate, [(0,-a["amount"])]+[(t,a["annual_operating_cash"]) for t in range(1,5)])
    tax_shield = value(yield_, shield_schedule)
    distress = value(rate,[(4,Q(a["distress_weight"])*a["distress_cost"])])
    rounded(unlevered,"10.245",3)
    rounded(tax_shield,"7.113",3)
    rounded(distress,"7.246",3)
    rounded(unlevered+tax_shield-distress-a["fee"],"7.112",3)
    rounded(unlevered+value(yield_,shield_schedule[:2])-distress-a["fee"],"3.795",3)

    # 14. Find all admissible bundles. Recheck resource and interaction perturbations.
    a = data["portfolio"]
    items = a["options_cost_days_npv"]

    def best(cash, days, require_any=(), synergy=None):
        candidates=[]
        for count in range(len(items)+1):
            for bundle in combinations(items, count):
                if require_any and not set(bundle).intersection(require_any):
                    continue
                sums=[sum(items[k][i] for k in bundle) for i in range(3)]
                adjust=synergy.get(bundle,0) if synergy else 0
                if sums[0]<=cash and sums[1]<=days:
                    candidates.append((sums[2]+adjust,bundle))
        return max(candidates)

    same(best(a["cash"],a["days"]),(64,("A","D")))
    same(best(a["cash"],a["days"]+1),(69,("A","B")))
    same(best(a["cash"]-1,a["days"]+1),(64,("A","D")))
    same(best(a["cash"]+10,a["days"]),(76,("A","C")))
    same(best(a["cash"],a["days"],synergy={("A","D"):-8}),(61,("B","C")))
    same(best(a["cash"],a["days"],require_any=("B","C")),(61,("B","C")))

    # 15. Terminal flow appears once, and equity is a separate bridge.
    def ev_components(forecast, rate, growth):
        r,g=Q(rate),Q(growth)
        if r<=g:
            raise ValueError("continuing growth must be below discount rate")
        tv=forecast[-1]*(1+g)/(r-g)
        dated=value(r,list(enumerate(forecast,1)))
        return tv,dated,value(r,[(len(forecast),tv)])

    a = data["enterprise"]
    tv, explicit, continuing=ev_components(a["cash_forecast"],a["rate"],a["growth"])
    ev=explicit+continuing
    equity=ev-a["debt_claim"]+a["excess_cash"]
    pps=equity*1000/a["shares"]
    rounded(tv,"847.33")
    rounded(explicit,"158.88")
    rounded(continuing,"578.74")
    rounded(ev,"737.62")
    rounded(pps,"15.14")
    same(round(100*continuing/ev),78)
    _,x,y=ev_components(a["cash_forecast"],".11",a["growth"])
    rounded(x+y,"647.74")
    rounded((x+y-a["debt_claim"]+a["excess_cash"])*1000/a["shares"],"12.89")
    _,stress_x,stress_y=ev_components(a["cash_forecast"],".12",a["growth"])
    same(continuing-stress_y > explicit-stress_x, True)
    try:
        ev_components(a["cash_forecast"],a["rate"],a["rate"])
    except ValueError:
        expected_checks += 1
    else:
        raise AssertionError("invalid terminal condition passed")

    # 16. Compare value, actual payment, and two separate cash dates.
    a = data["contingent_bid"]
    w, r, t = Q(a["trigger_weight"]), Q(a["payment_rate"]), a["years"]
    down, pay, single, floor = [a[k] for k in ("down_payment","trigger_pay","single","floor")]
    cont_price=down+value(r,[(t,w*pay)])
    rounded(cont_price,"435.87")
    rounded(a["operating_value"]-cont_price,"10.13")
    same(a["operating_value"]-single,16)
    same((a["cash_today"]-single,a["cash_today"]-down,a["cash_in_trigger"]-pay), (90,120,65))
    same(floor-(a["cash_in_trigger"]-pay),45)
    rounded((single-down)*(1+r)**t/w,"75.264",3)

    # 17. Algebraic spot-and-forward equivalence, not a return forecast.
    a = data["currency"]
    spot, usd, eur = [Q(a[k]) for k in ("spot_usd_per_eur","dollar_rate","euro_rate")]
    def forward(t):
        return spot*((1+usd)/(1+eur))**t
    flows=[(0,-a["cost_eur"]),(1,a["annual_receipt_eur"]),(2,a["annual_receipt_eur"])]
    er_value=value(eur,flows)
    usd_value=value(usd,[(t,forward(t)*c) for t,c in flows])
    same(spot*er_value,usd_value)
    rounded(usd_value,"5.50587",5)
    rounded(spot*value(usd,flows),"-1.85")
    delay=[(2,-10),(3,10)]
    same(value(eur,delay)*spot,value(usd,[(t,forward(t)*v) for t,v in delay]))
    rounded(value(eur,delay),"-0.50377",5)

    # 18. Distinguish eligibility, ratio, and counted cash.
    a = data["covenant"]
    gd,c,base,drop = [a[k] for k in ("gross_debt","eligible_cash","baseline_earnings","downside_earnings")]
    limit = Q(a["maximum_multiple"])
    nd = gd-c
    same((nd,limit*base-nd,nd-limit*drop),(230,43,20))
    rounded(Q(nd,base),"2.95")
    rounded(Q(nd,drop),"3.83")
    same((gd-20)-(c-20),nd)
    same(Q((gd-20)-c,drop),limit)
    same(Q(gd-(c+23),drop),Q("3.45"))

    # 19. Proceeds, fees, and transfer reconcile exactly.
    a = data["shares"]
    old,new,second,eq,fees = [a[k] for k in ("old_shares","new_shares","secondary_shares","old_equity_dollars","fees_dollars")]
    price=Q(a["offer_price"])
    net=new*price-fees
    pps=(eq+net)/(old+new)
    same((net, second*price, old+new),(420000,180000,500000))
    same(pps,Q("4.84"))
    same(eq-old*pps,(new*pps-new*price)+fees)
    same(((old+new)*Q(eq, old)-eq+fees)/new,Q("5.30"))

    # 20. Loan is fair before fee, but first eligible funding date can differ.
    a = data["board"]
    def project(prefix):
        return value(a[f"{prefix}_rate"], [(0,-a[f"{prefix}_order"])] +
                     [(t,a[f"{prefix}_annual_cash"]) for t in (1,2,3)] + [(3,a[f"{prefix}_sale"])])
    internal, route = project("internal"), project("route")
    lr, loan, fee=[Q(a[k]) for k in ("loan_rate","loan","loan_fee")]
    interest=loan*lr
    same(value(lr,[(0,loan)]+[(t,-interest) for t in (1,2,3)]+[(3,-loan)]),0)
    rounded(internal,"22.07")
    rounded(route,"25.38")
    rounded(route-fee,"21.38")
    same(route-fee<internal<route, True)
    cash=a["initial_cash"]
    w1,w2=a["base_week_movements"]
    il=a["internal_order"]
    rp=a["route_order"]
    f=loan-fee
    accel=a["acceleration"]
    same(balances(cash,-il,w1,w2),(180,130,165))
    same(balances(cash,-rp,w1,w2),(115,65,100))
    same(balances(cash,-rp+f,w1,w2),(166,116,151))
    same(balances(cash,-rp+f,w1+accel,w2-accel),(166,136,151))
    same(a["floor"]-min(balances(cash-20,-il,w1,w2)),20)
    same(a["floor"]-min(balances(cash-20,-rp+f,w1+accel,w2-accel)),14)

    # Supplementary review problems, with explicit conflicting verdicts.
    rv=value(".08", [(0,-125),(1,46),(2,49),(3,65)])
    rounded(rv,"11.20")
    rounded(rv-1,"10.20")
    same(balances(190,-125,-12,18),(65,53,71))
    same(balances(190,-126,-3,9),(64,61,70))
    same(balances(190,-128,-3,9),(62,59,68))
    same(max(fee for fee in range(10) if min(balances(190,-125-fee,-3,9))>=60),2)
    same((Q(160,50),Q("3.4")*50-160,20-(27-9)),(Q("3.2"),10,2))
    same(((182-8)-(22-8),160>Q("3.4")*46,150<=Q("3.4")*46),(160,True,True))
    _, ex0, ct0=ev_components([26,29,34],".09",".02")
    _, ex1, ct1=ev_components([26,29,34],".09",".03")
    rounded((ex0+ct0-90+16)*50/1000,"19.15")
    rounded((ex1+ct1-90+16)*50/1000,"22.56")
    rounded((ex0+ct0-90+8)*50/1000,"18.75")
    return expected_checks


if __name__ == "__main__":
    params = json.loads(DATA.read_text(encoding="utf-8"))
    print(f"{run(params)} exact/rounded rational checks passed for ten advanced chapters and three review problems.")
