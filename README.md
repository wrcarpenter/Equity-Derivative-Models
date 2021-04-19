# **EQUITY DERIVATIVE MODELS**

This repository implements lattice and Monte Carlo based models to price a variety of equity derivatives. Lattice methods refer specifically binomial and trinomial trees, which are most useful when considering American-style options.

The folder labeled "Code" provides the raw program code for various pricing models, implemented in both Python and MATLAB. See the "Notebooks" folder for implementation and exhibition of all models. 

## Cox Ross Rubenstein (CRR) Model

***INCOMPLETE and PRELIMINARY***

Binomial and Trinomial tree implementations of the acclaimed CRR model. Comparison to the Black-Scholes equation is included to see how the tree method performs relative to a
closed-form solution.

### The Binomial Model 

```python
def crr_binomial_tree(S, K, r, t, T, v, type, style)
```
Where the arguments are:
* S     : underlying price
* K     : strike price 
* r     : risk-less short rate 
* t     : number of periods 
* T     : option time-to-maturity (in yrs.)
* v     : annualized volatility
* otype : 'call' or 'put' option type (string argument)
* style : 'euro' or 'amer' option style (string argument)

### The Trinomial Model 
```python
def crr_trinomial_tree(S, K, r, t, T, vol, call, american)
```
Notice here that the function name is *trinomial* rather than binomial. Function arguments remain the same as in the binomial model (see previous section). 


### Visualizing CRR Trees


## Jarrow-Rudd  Model 

### The Binomial Model

A version of the CRR binomial model with p=1/2. 

## Option Payoffs 
This section is dedicated to dicussing different derivative payoffs. 

### European Calls and Puts

```python 
# European Call
max(S - K, 0)

# European Put
max(K - S, 0) 
```
Because of the symmetry of these payoffs, more compact code can be used that handles both types. Using a string function argument, a user can enter 'call' or 'put' that will implement the correct payoff.

```python 
# European call or put implementation

# User-defined argument for type of option 
if otype=='call': x = 1 
if otype=='put'; : x = -1 

# Option payoff function 
max(x*S - x*K, 0)
```
It is easy to see that inputting an agrument to define a variable 'x' will accomodate both types of option payoffs. 


# Data 

Historical stock price data acquired from Yahoo Finance. This can be utilized to calculate volatility. Riskless interest rates can be obtained from T-bill yields (under one year).

## Yahoo Finance Data 
[Yahoo Finance](https://finance.yahoo.com/) is an excellent source for historical equity prices and option chains, which include implied volatilties (presumably from inverting Black Scholes.

## Riskless Rates Data 
The [Treasury](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield) provides data on daily Treasury yield curve interest rates. 

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


## To Add

More granular comparison to Black-Scholes with graphs. 

Final price distributions for binomial and trinomial trees.

American options (calls/puts). 

Spread options. (two different trees with comparison of prices.).

Barrier options.

Asian options with monte carlo simulation of CRR (add some graphs as well). Lookback options with Monte Carlo.
