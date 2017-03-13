# -*- coding: utf-8 -*-
"""
@author: User
"""

n = 3

dice = range(1,7)
exp = sum(dice)/6.0

for i in range(1, n):
    exp = sum([exp if exp >= result else result for result in dice])/6.0

print exp