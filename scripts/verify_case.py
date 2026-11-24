"""Recompute the public draft's fictional case. No packages or network needed."""
from csv import DictReader
from decimal import Decimal
from pathlib import Path

D = Decimal
DATA = Path(__file__).resolve().parents[1] / "data" / "cooling-bay-case.csv"
RATE = D("0.10")
OPENING = D("300000")
RESERVE = D("90000")


def load(path=DATA):
    with Path(path).open(newline="", encoding="utf-8") as src:
        reader = DictReader(src)
        assert reader.fieldnames == ["option", "year", "component", "cash_dollars"]
        rows = {}
        for row in reader:
            k = row["option"], int(row["year"]), row["component"]
            v = D(row["cash_dollars"])
            if k in rows or not v.is_finite():
                raise ValueError(f"duplicate or invalid cash flow at {k}")
            rows[k] = v
    return rows


def result(rows, option, purchase_override=None, opening=OPENING):
    flows = {(year, component): value for (name, year, component), value in rows.items() if name == option}
    expected = {(0, "purchase"), (1, "operations"), (2, "operations"), (3, "operations"), (3, "sale")}
    if set(flows) != expected:
        raise ValueError(f"incomplete or undated {option} inputs")
    if purchase_override is not None:
        flows[0, "purchase"] = -D(purchase_override)
    npv = sum(value / ((1 + RATE) ** year) for (year, _), value in flows.items())
    post_purchase = opening + flows[0, "purchase"]
    return npv, post_purchase, post_purchase >= RESERVE


def main():
    rows = load()
    for option in ("compact", "whole_bay"):
        npv, cash, ok = result(rows, option)
        print(f"{option}: NPV ${npv:,.2f}; cash after payment ${cash:,.0f}; reserve {'passes' if ok else 'fails'}")
    npv, cash, ok = result(rows, "whole_bay", purchase_override=210000)
    print(f"transfer: NPV ${npv:,.2f}; cash after payment ${cash:,.0f}; reserve {'passes' if ok else 'fails'}")


if __name__ == "__main__":
    main()
