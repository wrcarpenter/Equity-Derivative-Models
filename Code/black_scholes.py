###################################################################
# BLACK-SCHOLES Option Pricing Formula
###################################################################

# Author      : Will Carpenter 
# Date Created: April 1st, 2021

# For pricing European call and put options.

import math
from scipy.stats import norm

# Black-Scholes Model

def black_scholes(S, K, r, T, t, v, x):

    d1 = (math.log(S/K) + (v**2/2 + r)*T)/(v*math.sqrt(T))
    d2 = d1 - v*math.sqrt(T)

    return x*S*norm.cdf(d1) - x*K*math.exp(-r*T)*norm.cdf(d2)


