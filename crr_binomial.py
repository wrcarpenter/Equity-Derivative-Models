
###################################################################
# COX-ROSS-RUBENSTEIN (CRR) Binomial Tree Implementation 
###################################################################

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
        St = S*u**(lastCol-row)*d**(row)
        crrTree[row, lastCol] =  max(x*St - x*K, 0)

    for col in range(lastCol-1, -1, -1):
        for row in range(0, col+1):
            # move backwards from previous prices 
            Pu = crrTree[row, col+1]
            Pd = crrTree[row+1, col+1]
            # Calcuate price on tree
            crrTree[row, col] = math.exp(-r*dt)*(p*Pu + (1-p)*Pd)

    return crrTree[0,0]

# Black-Scholes Model

def black_scholes(S, K, r, T, t, v, x):

    d1 = (math.log(S/K) + (v**2/2 + r)*T)/(v*math.sqrt(T))
    d2 = d1 - v*math.sqrt(T)

    return x*S*norm.cdf(d1) - x*K*math.exp(-r*T)*norm.cdf(d2)

# Monster Beverage 
crr_price = crr_binomial_tree(91.36, 95.00, 0.007, 15/252, 100, 0.8218, 1)
bs_price  =     black_scholes(91.36, 95.00, 0.007, 15/252, 100, 0.8218, 1)
print("________________________________________________________________\n")
print("Monster Beverage Corp.")
print("Expiry: June 18th")
print("CRR European Call Price: $" + "{:3.3f}".format(crr_price))
print("B-S European Call Price: $" + "{:3.3f}".format(bs_price))

# Carvana 
crr_price = crr_binomial_tree(265.32, 267.50, 0.00063, 15/252, 100, 0.6065, 1)
bs_price  =     black_scholes(265.32, 267.50, 0.00063, 15/252, 100, 0.6065, 1)
print("________________________________________________________________\n")
print("Carvana Co.")
print("Expiry: April 16th")
print("CRR European Call Price: $" + "{:3.2f}".format(crr_price))
print("B-S European Call Price: $" + "{:3.3f}".format(bs_price))

# American Airlines
crr_price = crr_binomial_tree(23.86, 24.00, 0.006, 15/252, 100, 0.5234, 1)
bs_price  =     black_scholes(23.86, 24.00, 0.006, 15/252, 100, 0.5234, 1)
print("________________________________________________________________\n")
print("American Airlines Group Inc.")
print("Expiry: April 23rd (15 days)")
print("European Call Price: $" + "{:3.2f}".format(crr_price))
print("B-S European Call Price: $" + "{:3.3f}".format(bs_price))
print("________________________________________________________________\n")

crr_price = crr_binomial_tree(91.36, 95.00, 0.007, 2.2/12, 100, 0.8218, 1)

def crr_build_tree(S, K, r, T, t, v, x):

    # s  : spot price 
    # k  : strike 
    # r  : riskless rate
    # T  : maturity (in yrs.)
    # t  : steps 
    # v  : annualized volatility

    # Calculate time increment 
    dt = T / t 
    # Initialize tree  
    crrTree, crrPrice         = np.empty((t,t)), np.empty((t,t)) 
    crrTree[:], crrPrice[:]   = np.nan, np.nan
    # Initial stock price
    crrTree[0,0] = S
    # Initialize tree parameters 
    u = math.exp(v*math.sqrt(dt))
    d = 1/u
    p = (math.exp(r*dt) - d)/(u - d)
    # Fill in top branch 
    for col in range(1,t):
        crrTree[0, col] = crrTree[0, col-1]*u
    # Fill in rest of tree
    for row in range(1, t):
        for col in range(row, t):
            crrTree[row, col] = crrTree[row-1, col-1]*d
    
    # European option payoff 
    lastCol = len(crrPrice)-1

    for row in range(0,lastCol+1):
        crrPrice[row, lastCol] =  max(crrTree[row, lastCol] - K, 0)

    discount = math.exp(-r*dt) 

    for col in range(lastCol-1, -1, -1):
        for row in range(0, col+1):
            # move backwards from previous prices 
            Su = crrPrice[row, col+1]
            Sd = crrPrice[row+1, col+1]
            # Calcuate price on tree
            crrPrice[row, col] = discount*(p*Su + (1-p)*Sd)

    #Testing code 
    print("u parameter: " "{:3.2f}".format(u))
    print("d parameter: " "{:3.2f}".format(d))
    print("p parameter: " "{:3.2f}".format(p))

    #print the stock price tree    
    print("\nCRR Stock Price Tree:\n")
    for i in crrTree:
        for j in i:
            print("{:7.2f}".format(j), end=" ")
        print() 
    print("\n")

    # print the stock price tree    
    print("\nCRR Option Price Tree:\n")
    for i in crrPrice:
        for j in i:
            print("{:7.2f}".format(j), end=" ")
        print() 
    print("\n")

    return crrPrice[0,0]

# Monster Beverage Call Option 
price    = crr_build_tree(91.36, 95.00, 0.007, 48/252, 15, 0.8218, 1)
bs_price = black_scholes(91.36, 95.00, 0.007, 48/252, 15, 0.8218, 1)
print("________________________________________________________________\n")
print("Monster Beverage Corp.")
print("Expiry: June 18th")
print("CRR European Call Price: $" + "{:3.2f}".format(price))
print("B-S European Call Price: $" + "{:3.2f}".format(bs_price))
print("________________________________________________________________\n")
