###################################################################
# Jarrow-Rudd (JR) Binomial Tree Implementation 
###################################################################

# Author      : Will Carpenter 
# Date Created: April 6th, 2021  

import math 
import numpy as np 
from scipy.stats import norm # cumulative normal distribution

def jr_binomial_tree(S, K, r, T, t, v, e):

    # S: initial asset price
    # K: strike price 
    # r: riskless rate 
    # T: time to maturity (in yrs.)
    # t: number of steps 
    # v: annualized volatility
    # e: euro call (= 1) euro put (= -1)

    # Calculate time increment 
    dt = T / t
    # Initialize tree  
    jrTree        = np.empty((t,t))
    jrTree[:]     = np.nan

    # Initialize tree parameters 
    u = math.exp((r - v**2/2)*dt + v*math.sqrt(dt))
    d = math.exp((r - v**2/2)*dt - v*math.sqrt(dt))
    p = 1/2

    lastCol = len(jrTree)-1

    for row in range(0,lastCol+1):
        St = S*u**(lastCol-row)*d**(row)
        jrTree[row, lastCol] =  max(e*St - e*K, 0)

    for col in range(lastCol-1, -1, -1):
        for row in range(0, col+1):
            # move backwards from previous prices 
            Pu = jrTree[row, col+1]
            Pd = jrTree[row+1, col+1]
            # Calcuate price on tree
            jrTree[row, col] = math.exp(-r*dt)*(p*Pu + (1-p)*Pd)

    return jrTree[0,0]
