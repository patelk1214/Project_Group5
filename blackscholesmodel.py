import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
import math 

PI = math.pi

def get_d1_d2(S, K, T, r, sigma): 
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    return d1, d2

def euro_vanilla(callput, S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
#     d1 = get_d1_d2(s, k, t, r, sigma)[0]
#     d2 = get_d1_d2(s, k, t, r, sigma)[1]
    
    if callput == 'call': 
        option_price = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    elif callput == 'put': 
        option_price = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    
    return option_price

def vega(S, d1, T): 
    
    pdf =(1/np.sqrt(2*math.pi)) * math.e**(0.5*d1**2)
    vega1 = S * pdf * np.sqrt(T)
    
    return vega1

def delta(callput, d1): 
    if callput == 'call': 
        return si.norm.cdf(d1, 0.0, 1.0) 
    elif callput == 'put': 
        return si.norm.cdf(d1, 0.0, 1.0) - 1

def implied_vol(callPut, S, K, r, option_price, T, hist_vol):
    
    initialGuess = hist_vol
    iterations = 10000
    tolerance = 0.0001
    iterCount = 0
    iterBool = True
    
    d1 = get_d1_d2(S, K, T, r, initialGuess)[0]
#     print(d1)
    while (iterCount < iterations) and iterBool: 
        
        iterCount = iterCount + 1
        BS1 = option_price - euro_vanilla(callPut, S, K, T, r, initialGuess)
        
        BSDiff1 = -vega(S, d1, T)
        newGuess = initialGuess - (BS1 / BSDiff1) 
        optionprice_diff = option_price - euro_vanilla(callPut, S, K, T, r, newGuess)
        
        initialGuess = newGuess
        
        if (abs(optionprice_diff) <= tolerance):
#             print("CONVERGES")
            iterBool = False
            return newGuess
          
        if iterBool and (iterCount == iterations):
#             print("Does not Converge")
            return 9999999

# if __name__ == '__main__':
    
#     s= 135.37
#     k = 135
#     r = 0.001
#     sigma = 0.27
#     t = 30/365
#     callput = 'call'
#     option_price = 3.95
#     hist_vol = 0.30
#     d1 = get_d1_d2(s, k, t, r, sigma)[0]

#     c = euro_vanilla(callput, s, k, t, r, sigma)
#     vol = implied_vol(callput, s, k, r, option_price, t, hist_vol)
#     # delta1 = delta(callput, d1)
#     vega = vega(s, d1, t) 

#     print(f'Call price: {c}')
#     print(f'Implied Vol : {vol}')
#     # print(f'Delta : {delta1}')
#     print(f'Vega : {vega}')