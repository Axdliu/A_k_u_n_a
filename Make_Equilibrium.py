# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 01:11:51 2017

@author: User
"""

def mkt_equil(mkt_share, probs):
    for i in range(100):
        mkt_new = [0]*len(mkt_share)
        for k in range(len(mkt_share)):
            mkt_temp = [i*mkt_share[k] for i in probs[k]]
            mkt_new = map(lambda a,b:a+b, mkt_temp, mkt_new)
        mkt_share = mkt_new
    return [round(i,4) for i in mkt_share]


mkt_share1 = [.4, .6]
prob1 = [[.8,.2],[.1,.9]]
    
mkt_share2 = [.12, .14, .51, .23]
prob2 = [[.10, .20, .30, .40],
        [.25, .25, .25, .25],
        [.30, .30, .30, .10],
        [.05, .15, .25, .55]
        ]

mkt_share, probs = mkt_share1, prob1
print mkt_equil(mkt_share, probs)

# mkt_share, probs = mkt_share2, prob2
# print mkt_equil(mkt_share, probs), sum(mkt_equil(mkt_share, probs))

""" _____________________________________________________________________ """

import pandas as pd

pd2 = pd.DataFrame(prob2)
pd2.sum(axis=1)