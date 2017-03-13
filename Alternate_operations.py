# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 15:41:03 2017
n = 4
((1+2)*3)-4 = 5

@author: User
"""

import itertools

def alt_operation(n):
    
    ops = {"+": (lambda x,y: x+y), "*": (lambda x,y: x*y), "-": (lambda x,y: x-y)}
    k = itertools.cycle('+*-')       
           
    if n < 2:
        return 1
    else:
        result = 1
        for n in range(2,n+1):
            result = ops[next(k)](result, n)
        return result
        
n = 4
print alt_operation(n)

