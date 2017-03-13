# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 16:55:48 2017

@author: User
"""

import math

def gen():
    yield {1,2,3,4}
    yield {(1,2,3,4)}
    yield {1:2, 3:4}
    yield {(1,2),(3,4)}
    yield set([1,2,3])
    yield {math.log(x) for x in range(1,10)}
    yield {}

x = gen()

for i in range(7):
    test = next(x)
    print test, type(test)
