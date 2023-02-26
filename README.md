# **Equity Derivative Models**

Options are a must-know for any financial practioner, especially traders. They are quite prevalant outside of equities, in fixed income deratives and mortgaged-based securities. In fact, anyone who takes out of a mortgage has effectively bought an embedded option on rates!

This repository implements lattice and Monte Carlo based models to price a variety of equity derivatives. Lattice methods refer specifically binomial and trinomial trees, which are most useful when considering American-style options.

The folder labeled "Code" provides the raw program code for various pricing models, implemented in both Python and MATLAB. See the "Notebooks" folder for implementation and exhibition of all models. 

## Cox Ross Rubenstein (CRR) Model

The Cox-Ross-Rubenstein (CRR) model is one of the most well-known binomial option pricing schemes in finance.  

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

#### Parameters
Tree dynamics are governed by three parameters: probability (p), up-move (u), down-move (d). These arederived such that the tree dynamics converge to Black-Scholes as the time increment (t) becomes infinitely small. 
```python
#  v ~ volatility 
# dt ~ time increment (T/t)

# risk-neutral probability 
p = (math.exp(r * dt) - d)/(u - d)
# up
u = math.exp(v * math.sqrt(dt))
# down 
d = 1 / u
```


### The Trinomial Model 
```python
def crr_trinomial_tree(S, K, r, t, T, vol, call, american)
```
Notice here that the function name is *trinomial* rather than binomial. Function arguments remain the same as in the binomial model (see previous section). 


### Visualizing CRR Trees

## Jarrow-Rudd  Model 

### The Binomial Model

A particular adaptation of the CRR binomial model where it is assumed that the risk neutral probability is equal for the up and down states (p=1/2). This assumption generates the following parameters to govern tree dymamics:

#### Parameters
```python
#  v ~ annualized volatility 
# dt ~ time increment (T/t)

# risk-neutral probability 
p = 1/2
# up
u = math.exp(v * math.sqrt(dt))
# down 
d = 1 / u
```

## Option Payoffs 
This section is dedicated to dicussing different derivative payoffs. 


| Type | Style | Payoff |  Wiki  |
| --- | --- | --- | --- |
| European | Call | $max(S(T) - K, 0)$ |  null |
| European | Put | $max(K - S(T), 0)$ |  null |
| American | Put | $max(S(t) - K, optionValue)$ |  null |

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
if otype=='call' : x = 1 
if otype=='put'  : x = -1 

# Option payoff function 
max(x * S - x * K, 0)
```
It is easy to see that inputting an agrument to define a variable 'x' will accomodate both types of option payoffs. 

# Data 

Historical stock price data acquired from Yahoo Finance. This can be utilized to calculate volatility. Riskless interest rates can be obtained from T-bill yields (under one year).

## Yahoo Finance 
[Yahoo Finance](https://finance.yahoo.com/) is an excellent source for historical equity prices and option chains, which include implied volatilties (presumably from inverting the Black-Scholes formula).

## Google Finance
[Google Finance](https://www.google.com/finance/) provides an API within its spreadsheet software (Google Sheets) to pull historical equity data.

## Riskless Interest Rates 
The [US Treasury](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield) provides data on daily Treasury yield curve interest rates. These rates are considered to be the par-yields on 'constant-maturity' Treasury securities.  

## To Add

* Valuation is "fair" price given all available information, not "true" price for a security. Fair is based on reasonable assumptions (log-normal distribution of returns, etc.) and accurate analysis of current market dynamics (stock volatility, risk-free interest rate, etc.). Without a crystal ball, it is impossible to know the true price for something. Uncertainty of the future always makes prices random variables, i.e. variables that can take on a range of values with associated probabilties.

* simple "naked" option payoff tables (w/ bearish and bullish interpretations)

* Excel spreadsheets for tree testing and design

* Quant education --> heston model clean explanation

* Calculate option greeks: vega, theta, delta, gamma.

* Invert Black-Scholes function ~ ivol(...) 

* More granular comparison to Black-Scholes with graphs. 

* Final price distributions for binomial and trinomial trees.

* American options (calls/puts). 

* Spread options. (two different trees with comparison of prices.).

* Barrier options.

* Asian options with monte carlo simulation of CRR (add some graphs as well). Lookback options with Monte Carlo.
