#!/usr/bin/env python3
"""Zero-dependency pip value / position size calculator.

Reads data/contract-specs.json from its own directory. Standard library only.
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "contract-specs.json")


def load():
    with open(DATA, encoding="utf-8") as fh:
        doc = json.load(fh)
    return {i["instrument"]: i for i in doc["instruments"]}


def fmt_money(v, ccy):
    return "%.2f %s" % (v, ccy)


def main():
    p = argparse.ArgumentParser(
        description="Pip value, position size and margin for forex and metals.")
    p.add_argument("instrument", nargs="?", help="e.g. EURUSD, USDJPY, XAUUSD")
    p.add_argument("--lots", type=float, default=1.0, help="lot size (default 1.0)")
    p.add_argument("--pips", type=float, default=1.0, help="number of pips (default 1)")
    p.add_argument("--balance", type=float, help="account balance")
    p.add_argument("--risk-percent", type=float, help="risk per trade, in percent")
    p.add_argument("--stop-pips", type=float, help="stop loss distance in pips")
    p.add_argument("--leverage", type=float, help="leverage as a ratio, e.g. 100 for 1:100")
    p.add_argument("--price", type=float, help="current price, needed for margin")
    p.add_argument("--json", action="store_true", help="emit JSON")
    p.add_argument("--list", action="store_true", help="list supported instruments")
    a = p.parse_args()

    spec = load()

    if a.list or not a.instrument:
        for k in sorted(spec):
            s = spec[k]
            print("%-7s pip=%-7s contract=%-8s quote=%s" % (
                k, "%g" % s["pip_size"], format(int(s["contract_size"]), ","),
                s["quote_currency"]))
        if not a.instrument:
            return 0
        return 0

    key = a.instrument.upper()
    if key not in spec:
        sys.stderr.write("Unknown instrument: %s (try --list)\n" % a.instrument)
        return 2

    s = spec[key]
    ccy = s["quote_currency"]
    pip_per_lot = s["pip_size"] * s["contract_size"]
    pip_value = pip_per_lot * a.lots
    point_value = pip_value / 10.0
    position_size = a.lots * s["contract_size"]

    out = {
        "instrument": key,
        "pip_size": s["pip_size"],
        "contract_size": s["contract_size"],
        "quote_currency": ccy,
        "lots": a.lots,
        "pip_value_per_lot": pip_per_lot,
        "pip_value": pip_value,
        "point_value": point_value,
        "position_size": position_size,
    }

    if a.pips:
        out["move_value"] = pip_value * a.pips

    if a.balance and a.risk_percent and a.stop_pips:
        risk_amount = a.balance * a.risk_percent / 100.0
        stop_money = a.stop_pips * pip_per_lot
        lots = risk_amount / stop_money if stop_money else 0.0
        lots = int(lots * 100) / 100.0  # round down to 0.01
        out.update({
            "risk_amount": risk_amount,
            "stop_loss_in_money_per_lot": stop_money,
            "suggested_lot_size": lots,
            "suggested_position_size": lots * s["contract_size"],
        })
        if a.leverage and a.price:
            out["margin_required"] = (lots * s["contract_size"] * a.price) / a.leverage

    if a.json:
        print(json.dumps(out, indent=2))
        return 0

    print("Instrument            %s" % key)
    print("Pip size              %g" % s["pip_size"])
    print("Contract size         %s" % format(int(s["contract_size"]), ","))
    print("Lots                  %g" % a.lots)
    print("Pip value per lot     %s" % fmt_money(pip_per_lot, ccy))
    print("Pip value             %s" % fmt_money(pip_value, ccy))
    print("Point value           %s" % fmt_money(point_value, ccy))
    print("Position size         %s units" % format(int(position_size), ","))
    if "move_value" in out:
        print("Value of %g pip move    %s" % (a.pips, fmt_money(out["move_value"], ccy)))
    if "suggested_lot_size" in out:
        print("")
        print("Risk amount           %.2f" % out["risk_amount"])
        print("Stop loss per lot     %s" % fmt_money(out["stop_loss_in_money_per_lot"], ccy))
        print("Suggested lot size    %.2f" % out["suggested_lot_size"])
        print("Suggested position    %s units" % format(int(out["suggested_position_size"]), ","))
    if "margin_required" in out:
        print("Margin required       %.2f" % out["margin_required"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
