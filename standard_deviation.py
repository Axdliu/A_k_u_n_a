# -*- coding: utf-8 -*-
"""
对于输入的所有float, 求standard deviation

@author: User
"""

numlist = (23, 4, 4, 54.54, 43)
import math
def SD(numlist):
    avg = float(sum(numlist))/len(numlist)
    var = 0
    for i in numlist:
        var += pow(i-avg,2)
    return math.sqrt(var/len(numlist))

# checking result
import numpy
print SD(numlist)
print numpy.std(numlist)

