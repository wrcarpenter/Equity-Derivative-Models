# **EQUITY OPTION MODELS**

## Cox Ross Rubenstein (CRR) Model

***INCOMPLETE and PRELIMINARY***

Binomial and Trinomial tree implementations of the acclaimed CRR model. Comparison to the Black-Scholes equation is included to see how the tree method performs relative to a
closed-form solution.

### The Binomial Model 

```python
def crr_build_tree(S, K, r, t, T, vol, call, american)
```
Where the arguments are:
* S : underlying price
* K : strike price 
* r : risk-less short rate 
* t : number of periods 
* T : option time-to-maturity (in yrs.)
* vol : annualized volatility
* call : 'call' or 'put' (string argument)
* american : European (=0) or American (=1)

### The Trinomial Model 

### Visualizing CRR Trees


## Jarrow-Rudd  Model 

### The Binomial Model

A version of the CRR binomial model with p=1/2. 

# Data 

Historical stock price data acquired from Yahoo Finance. This can be utilized to calculate volatility. Riskless interest rates can be obtained from T-bill yields (under one year).

## Yahoo Finance Data 
Equity historical prices and option chains (including implied volatilties):
* https://finance.yahoo.com/

A more rigorous continuously compounding riskless interest rates can be acquired from on-the-run Treasury data via interpolatoin and bootstrapping. 

## Options Chain Examples 

See below for the options data on equities implemented within this projects notebooks for the CRR and JR models: 

| Company | Ticker | Industry |  Options Chain  | Historical Stock Price Data | 
| --- | --- | --- | --- | --- |
| American Airlines | `AAL` | Aviation |  [options](https://finance.yahoo.com/quote/AAL/options/)  |  [price data](https://finance.yahoo.com/quote/AAL/history?p=AAL) |
| Norweigian Cruise Line | `NCLH` | Cruise lines | | |
| Newmont Corporation | `NCLH` | Gold mining | | |
| Lithium Americas Corp. | `ticker` | Lithium mining | | |
| McDonald's Corp. | `ticker` | Fast-food | | |
| Coca-Cola Corp. | `ticker` | Food & Beverage | | |
| Carvana | `ticker` | Auto retail | | |
| Credit Acceptance Corp. | `CACC` | Auto finance | | |
| Banco Santander | `SAN` | Retail banking | | |
| Simon Property Group | `SPG` | Real estate| | |

# To Add

More granular comparison to Black-Scholes with graphs. 

Final price distributions for binomial and trinomial trees.

American options (calls/puts). 

Spread options. (two different trees with comparison of prices.).

Barrier options.

Asian options with monte carlo simulation of CRR (add some graphs as well). Lookback options with Monte Carlo.

* american : European (=0) or American (=1)
