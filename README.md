# forex-contract-specs

Machine-readable pip sizes and contract sizes for 30 forex and metals instruments,
plus a zero-dependency CLI that computes pip value, position size and margin.

The problem this solves: pip size and contract size are conventions, not prices. They are
scattered across broker pages, disagree at the edges (JPY pairs, silver), and are almost never
available in a form you can pipe into a script. This repo puts them in CSV, JSON and Markdown.

## Contents

| File | What it is |
|---|---|
| `data/pip-values.csv` | 30 instruments: pip size, contract size, quote currency, pip value at standard / mini / micro |
| `data/contract-specs.json` | Same data as JSON, with a `source_note` describing the conventions |
| `data/CONTRACT-SPECS.md` | Human-readable table, plus the conventions actually used |
| `data/breakeven-win-rate.csv` | Risk/reward ratio 1:1 to 1:5 against the win rate needed to break even |
| `pipvalue.py` | Zero-dependency Python CLI |

## Install

Nothing to install. `pipvalue.py` uses only the standard library and reads
`data/contract-specs.json` from its own directory.

```bash
git clone https://github.com/OWNER/forex-contract-specs.git
cd forex-contract-specs
```

Requires Python 3.7 or newer.

## Usage

```bash
# pip value for one standard lot of EURUSD
python pipvalue.py EURUSD

# 0.35 mini lots of USDJPY, and the value of a 24 pip move
python pipvalue.py USDJPY --lots 0.35 --pips 24

# position size and margin from a risk budget instead
python pipvalue.py GBPUSD --balance 10000 --risk-percent 1 --stop-pips 20 --leverage 100

# list every supported instrument
python pipvalue.py --list
```

Output is plain text on stdout, so it pipes into anything:

```bash
python pipvalue.py EURUSD --json | jq .pip_value_standard_lot
```

## Conventions

These are the conventions this dataset follows. They are stated explicitly because sources
disagree, and silently mixing conventions is how position sizing bugs get shipped.

- Pairs quoted to four decimals use a pip size of `0.0001`. JPY pairs are quoted to two
  decimals, so a pip is `0.01`.
- `XAUUSD` and `XAGUSD` follow the two-decimal convention: a pip is a `0.01` move in price.
  Some tools and brokers call the `0.001` digit on silver a pip instead.
- A point is one tenth of a pip — the last decimal your broker shows.
- Pip values are stated in the **quote currency of the pair**, before conversion into any
  account currency. Converting into your own currency needs a live rate, which is deliberately
  out of scope here.

## Formulas

```
pip value per lot   = pip size x contract size
pip value           = pip size x contract size x lots
position size       = lots x contract size
risk amount         = balance x risk percent
stop loss in money  = stop pips x pip value per lot
lot size            = risk amount / stop loss in money
margin required     = position value / leverage
breakeven win rate  = 1 / (1 + R)
```

## Interactive version

If you want the same numbers without running anything, the browser version of these
calculators lives at <https://lotcalculator.net>.

## License

MIT. The data is factual convention data and is published for reuse without restriction.
