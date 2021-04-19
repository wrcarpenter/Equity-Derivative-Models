# Cox Ross Rubenstein (CRR) Model

***INCOMPLETE and PRELIMINARY***

Binomial and Trinomial tree implementations of the acclaimed CRR model. Comparison to the Black-Scholes equation is included to see how the tree method performs relative to a
closed-form solution.

```python
crr_build_tree(S, K, r, t, T, vol, call, american)
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

## Jarrow-Rudd Model 

A version of the CRR binomial model with p=1/2. 

# Data 

Historical stock price data acquired from Yahoo Finance. This can be utilized to calculate volatility. Riskless interest rates can be obtained from T-bill yields (under one year).

## Yahoo Finance Data 
Equity historical prices and option chains (including implied volatilties):
* https://finance.yahoo.com/

A more rigorous continuously compounding riskless interest rates can be acquired from on-the-run Treasury data via interpolatoin and bootstrapping. 

## Options Chain Examples 

See below for the options data on equities implemented within this projects notebooks for the CRR and JR models: 

| Company | Ticker |  Options Chain  | Historical Prices | 
| --- | --- | --- | --- |
| `git status` | List all *new or modified* files | |  |
| `git diff` | Show file differences that **haven't been** staged | | | 

**American Airlines** 
* [options chain](https://finance.yahoo.com/quote/AAL/options/)
* International airline 

**Norwegian Cruise Line**
* https://finance.yahoo.com/quote/NCLH/options/
* International cruise line 

**Newmont Corporation** 
* https://finance.yahoo.com/quote/NEM/options/
* World's largest gold mining company

**Lithium Americas Corp**
* https://finance.yahoo.com/quote/LAC/options/
* Canadian Lithium mining company 

**Mcdonald's Corp**
* https://finance.yahoo.com/quote/MCD/options/
* American fast-food company 

**Coca-Cola Consolidated Inc**
* https://finance.yahoo.com/quote/KO/options/
* Soda beverage manufacturer

**Carvana** 
* https://finance.yahoo.com/quote/CVNA/options/
* Online used car retailer based in Tempe, Arizona.


# To Add

More granular comparison to Black-Scholes with graphs. 

Final price distributions for binomial and trinomial trees.

American options (calls/puts). 

Spread options. (two different trees with comparison of prices.).

Barrier options.

Asian options with monte carlo simulation of CRR (add some graphs as well). Lookback options with Monte Carlo.

```python
crr_build_tree(r, K, S, t, T, vol, call, american)
```
Where we would have:
* r : risk free rate 
* K : strike price 
* S : underlying price 
* t : time increment
* vol : annualized volatility
* call : call (=1) or put (=0)
* american : European (=0) or American (=1)
