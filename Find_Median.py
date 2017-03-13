# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 00:58:32 2017

@author: User
"""

input_list = range(10)
k = 6

def find_median(input_list, k):
    subset = input_list[:input_list.index(k)+1]
    if len(subset)%2 == 0:
        median = (subset[len(subset)//2]+subset[len(subset)//2-1])/2.0
    else:
        median = subset[len(subset)//2]
    return median

print find_median(input_list, k)



def find_median(input_list, k):
    subset = input_list[:input_list.index(k)+1]
    while len(subset) >= 3:
        subset.pop(0)
        subset.pop()
    if len(subset) == 1:
        return subset[0]
    if len(subset) == 2:
        return sum(subset)/2.0

input_list = range(10)
k = 6
print find_median(input_list, k)