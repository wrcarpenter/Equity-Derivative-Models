# Cox Ross Rubenstein (CRR) Model

***INCOMPLETE and PRELIMINARY***

Binomial and Trinomial tree implementations of the acclaimed CRR model. Comparison to the Black-Scholes equation is included to see how the tree method performs relative to a
closed-form solution.

Pricing: European calls/puts, American calls/puts, barrier options. 


## Jarrow-Rudd Model 

A version of the CRR binomial model with p=1/2. 

# Data 

Historical stock price data acquired from Yahoo Finance. This can be utilized to calculate volatility.

Continuously compounding riskless interest rates can be acquired from on-the-run Treasury data via interpolatoin and bootstrapping. 

# To Add

More granular comparison to Black-Scholes with graphs. 

Final price distributions for binomial and trinomial trees.

American options (calls/puts). 

Spread options. (two different trees with comparison of prices.).

Barrier options.

Asian options with monte carlo simulation of CRR (add some graphs as well). Lookback options with Monte Carlo.

```python
crr_build_tree(r, K, S, t)
```
