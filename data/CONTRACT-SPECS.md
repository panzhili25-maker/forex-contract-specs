# Contract specifications

Pip size and contract size for 30 instruments: 28 currency pairs plus gold (XAUUSD) and silver (XAGUSD).

Pip values below are stated in the **quote currency of the pair**, before any conversion into your account currency. Pip size and contract size are fixed conventions, so these numbers do not drift with the market.

| Instrument | Pip size | Contract size | Quote | Standard (1.0) | Mini (0.1) | Micro (0.01) |
|---|---|---|---|---|---|---|
| EURUSD | 0.0001 | 100,000 | USD | 10.00 USD | 1.00 USD | 0.10 USD |
| GBPUSD | 0.0001 | 100,000 | USD | 10.00 USD | 1.00 USD | 0.10 USD |
| USDJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| USDCHF | 0.0001 | 100,000 | CHF | 10.00 CHF | 1.00 CHF | 0.10 CHF |
| USDCAD | 0.0001 | 100,000 | CAD | 10.00 CAD | 1.00 CAD | 0.10 CAD |
| AUDUSD | 0.0001 | 100,000 | USD | 10.00 USD | 1.00 USD | 0.10 USD |
| NZDUSD | 0.0001 | 100,000 | USD | 10.00 USD | 1.00 USD | 0.10 USD |
| EURGBP | 0.0001 | 100,000 | GBP | 10.00 GBP | 1.00 GBP | 0.10 GBP |
| EURJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| EURCHF | 0.0001 | 100,000 | CHF | 10.00 CHF | 1.00 CHF | 0.10 CHF |
| EURAUD | 0.0001 | 100,000 | AUD | 10.00 AUD | 1.00 AUD | 0.10 AUD |
| EURCAD | 0.0001 | 100,000 | CAD | 10.00 CAD | 1.00 CAD | 0.10 CAD |
| EURNZD | 0.0001 | 100,000 | NZD | 10.00 NZD | 1.00 NZD | 0.10 NZD |
| GBPJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| GBPCHF | 0.0001 | 100,000 | CHF | 10.00 CHF | 1.00 CHF | 0.10 CHF |
| GBPAUD | 0.0001 | 100,000 | AUD | 10.00 AUD | 1.00 AUD | 0.10 AUD |
| GBPCAD | 0.0001 | 100,000 | CAD | 10.00 CAD | 1.00 CAD | 0.10 CAD |
| GBPNZD | 0.0001 | 100,000 | NZD | 10.00 NZD | 1.00 NZD | 0.10 NZD |
| AUDJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| AUDCHF | 0.0001 | 100,000 | CHF | 10.00 CHF | 1.00 CHF | 0.10 CHF |
| AUDCAD | 0.0001 | 100,000 | CAD | 10.00 CAD | 1.00 CAD | 0.10 CAD |
| AUDNZD | 0.0001 | 100,000 | NZD | 10.00 NZD | 1.00 NZD | 0.10 NZD |
| CADJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| CADCHF | 0.0001 | 100,000 | CHF | 10.00 CHF | 1.00 CHF | 0.10 CHF |
| CHFJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| NZDJPY | 0.01 | 100,000 | JPY | 1000.00 JPY | 100.00 JPY | 10.00 JPY |
| NZDCHF | 0.0001 | 100,000 | CHF | 10.00 CHF | 1.00 CHF | 0.10 CHF |
| NZDCAD | 0.0001 | 100,000 | CAD | 10.00 CAD | 1.00 CAD | 0.10 CAD |
| XAUUSD | 0.01 | 100 | USD | 1.00 USD | 0.10 USD | 0.01 USD |
| XAGUSD | 0.01 | 5,000 | USD | 50.00 USD | 5.00 USD | 0.50 USD |

## Conventions

* Currency pairs quoted to 4 decimals use a pip size of 0.0001. JPY pairs are quoted to 2 decimals, so a pip is 0.01.
* XAUUSD and XAGUSD follow the two-decimal convention used here: a pip is a 0.01 move in price. Some tools and brokers call the 0.001 digit on silver a pip instead.
* A point is one tenth of a pip: the last decimal your broker shows.
