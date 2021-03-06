# Cox-Ross-Rubenstein Binomial Tree 

# Author      : Will Carpenter 
# Date Created: April 1st, 2021  

import math 
import numpy as np 
from scipy.stats import norm # cumulative normal distribution

def crr_binomial_tree(S, K, r, T, t, v, x):

    # S: initial asset price
    # K: strike price 
    # r: riskless rate 
    # T: time to maturity (in yrs.)
    # t: number of steps 
    # v: annualized volatility
    # x: euro call (= 1) euro put (= -1)

    # Calculate time increment 
    dt = T / t
    # Initialize tree  
    crrTree        = np.empty((t,t))
    crrTree[:]     = np.nan

    # Initialize tree parameters 
    u = math.exp(v*math.sqrt(dt))
    d = 1/u
    p = (math.exp(r*dt) - d)/(u - d)

    lastCol = len(crrTree)-1

    for row in range(0,lastCol+1):
        # Calculate prices at the end of the tree
        St = S*u**(lastCol-row)*d**(row)
        # Determine terminal tree payoffs 
        crrTree[row, lastCol] =  max(x*St - x*K, 0)

    for col in range(lastCol-1, -1, -1):
        for row in range(0, col+1):
            # backward iteration from end of tree
            Pu = crrTree[row, col+1]
            Pd = crrTree[row+1, col+1]
            # Calcuate price on at tree node
            crrTree[row, col] = math.exp(-r*dt)*(p*Pu + (1-p)*Pd)

    return crrTree[0,0]
