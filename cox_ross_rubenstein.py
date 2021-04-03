###################################################################
# COX-ROSS-RUBENSTEIN (CRR) Binomial Tree Implementation 
###################################################################

# Author      : Will Carpenter 
# Date Created: April 1st, 2021  

import math 
import numpy as np

def crr_tree(s, k, r, T, t, v):

    # s  : spot price 
    # k  : strike 
    # r  : riskless rate
    # T  : maturity (in yrs.)
    # t : steps 
    # v  : annualized volatility

    # Calculate time increment 
    dt = T / t 
    # Initialize tree  
    crrTree      = np.empty((t,t)) 
    crrPrice     = np.empty((t,t))
    crrTree[:]   = np.nan
    crrPrice[:]  = np.nan
    
    crrTree[0,0] = s

    # Initialize tree parameters 
    u = math.exp(v*math.sqrt(dt))
    d = 1/u
    p = (math.exp(r*dt) - d)/(u - d)

    # Fill in top branch 
    for col in range(1,t):
        crrTree[0, col] = crrTree[0, col-1]*u
    
    for row in range(1, t):
        for col in range(row, t):
            crrTree[row, col] = crrTree[row-1, col-1]*d
    
    # European option payoff 
    
    lastCol = len(crrPrice)-1

    for row in range(0,lastCol+1):
        crrPrice[row, lastCol] =  max(crrTree[row, lastCol] - k, 0)

    discount = math.exp(-r*dt) 

    for col in range(lastCol-1, -1, -1):
        for row in range(0, col+1):
            # move backwards from previous prices 
            Pu = crrPrice[row, col+1]
            Pd = crrPrice[row+1, col+1]
            # Calcuate price on tree
            crrPrice[row, col] = discount*(p*Pu + (1-p)*Pd)

    
    return crrPrice[0,0]


    # Testing code 
    # print(u)
    # print(d)
    # print(p)

    # print the stock price tree    
    # print("\nCRR Stock Price Tree:\n")
    # for i in crrTree:
    #     for j in i:
    #         print("{:3.2f}".format(j), end=" ")
    #     print() 
    # print("\n")

    # # print the stock price tree    
    # print("\nCRR Option Price Tree:\n")
    # for i in crrPrice:
    #     for j in i:
    #         print("{:3.2f}".format(j), end=" ")
    #     print() 
    # print("\n")

# Testing 

# Monster Beverage Call Option 
price = crr_tree(91.36, 95.00, 0.007, 2.5/12, 100, 0.2753)
print("--------------------------------------------------------------")
print("Monster Beverage Corp.")
print("Expiry: June 18th")
print("European Call Price: $" + "{:3.2f}".format(price))

price = crr_tree(265.32, 267.50, 0.0007, 0.217/12, 50, 0.5620)
print("--------------------------------------------------------------")
print("Carvana Co.")
print("Expiry: April 9th")
print("European Call Price: $" + "{:3.2f}".format(price))
print("--------------------------------------------------------------")
