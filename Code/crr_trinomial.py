###################################################################
# COX-ROSS-RUBENSTEIN (CRR) Trinomial Tree Implementation 
###################################################################

# Author      : Will Carpenter 
# Date Created: April 1st, 2021  

import math 
import numpy as np 
from scipy.stats import norm # cumulative normal distribution

def crr_trinomial_tree(S, K, r, T, t, v, x):

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
    crrTree        = np.empty((2*t-1,t))
    crrTree[:]     = np.nan

    # Initialize tree parameters 
    u = math.exp(v*math.sqrt(2*dt))
    d = 1/u
    m = 1
    # Probability-up
    pu = ((math.exp(r*dt/2) - math.exp(-1*v*math.sqrt(dt/2))) / 
         (math.exp(v*math.sqrt(dt/2)) - math.exp(-1*v*math.sqrt(dt/2))))**2
    # Probability-down
    pd = ((math.exp(v*math.sqrt(dt/2)) - math.exp(r*dt/2)) /
         (math.exp(v*math.sqrt(dt/2)) - math.exp(-1*v*math.sqrt(dt/2))))**2
    # Probability-middle
    pm = 1 - (pu + pd)

    lastCol = crrTree.shape[1]-1
    mid     = len(crrTree)//2

    # Set price at middle of tree 
    crrTree[mid, lastCol] = max(x*S-x*K, 0)

    for i in range(1, mid+1):
        crrTree[mid-i, lastCol] = max(x*S*u**i - x*K, 0)
        crrTree[mid+i, lastCol] = max(x*S*d**i - x*K, 0)

    for col in range(lastCol-1, -1, -1):
        for row in range(0, col*2+1):
            # move backwards from previous prices 
            Su = crrTree[row,   col+1]
            Sm = crrTree[row+1, col+1]
            Sd = crrTree[row+2, col+1]
            # Calcuate price on tree
            crrTree[row, col] = math.exp(-r*dt)*(pu*Su + pm*Sm + pd*Sd)

    # print("u parameter: " "{:6.4f}".format(u))
    # print("d parameter: " "{:6.4f}".format(d))
    # print("pu parameter: " "{:5.3f}".format(pu))
    # print("pd parameter: " "{:5.3f}".format(pd))
    # print("pm parameter: " "{:5.3f}".format(pm))
    # print("pm+pu+pd: " "{:9.3f}".format(pm+pu+pd))


    # print("\nCRR Stock Price Tree:\n")
    # for i in crrTree:
    #     for j in i:
    #         print("{:7.2f}".format(j), end=" ")
    #     print() 
    # print("\n")

    return crrTree[0,0]

# Black-Scholes Model

def black_scholes(S, K, r, T, t, v, x):

    d1 = (math.log(S/K) + (v**2/2 + r)*T)/(v*math.sqrt(T))
    d2 = d1 - v*math.sqrt(T)

    return x*S*norm.cdf(d1) - x*K*math.exp(-r*T)*norm.cdf(d2)

# Monster Beverage 
crr_price = crr_trinomial_tree(91.36, 95.00, 0.007, 15/252, 100, 0.8218, 1)
bs_price  =     black_scholes(91.36, 95.00, 0.007, 15/252, 100, 0.8218, 1)
print("________________________________________________________________\n")
print("Monster Beverage Corp.")
print("Expiry: June 18th")
print("CRR European Call Price: $" + "{:3.3f}".format(crr_price))
print("B-S European Call Price: $" + "{:3.3f}".format(bs_price))

# Carvana 
crr_price = crr_trinomial_tree(265.32, 267.50, 0.00063, 15/252, 100, 0.6065, 1)
bs_price  =     black_scholes(265.32, 267.50, 0.00063, 15/252, 100, 0.6065, 1)
print("________________________________________________________________\n")
print("Carvana Co.")
print("Expiry: April 16th")
print("CRR European Call Price: $" + "{:3.2f}".format(crr_price))
print("B-S European Call Price: $" + "{:3.3f}".format(bs_price))

# American Airlines
crr_price = crr_trinomial_tree(23.86, 24.00, 0.006, 15/252, 100, 0.5234, 1)
bs_price  =     black_scholes(23.86, 24.00, 0.006, 15/252, 100, 0.5234, 1)
print("________________________________________________________________\n")
print("American Airlines Group Inc.")
print("Expiry: April 23rd (15 days)")
print("European Call Price: $" + "{:3.2f}".format(crr_price))
print("B-S European Call Price: $" + "{:3.3f}".format(bs_price))
print("________________________________________________________________\n")
