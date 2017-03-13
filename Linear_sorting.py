# -*- coding: utf-8 -*-
"""
an array A of n unique integers, sort and print the
array in O(m) time. 

max(A) - min(A) < m
integers all > 0
no built-in libraries

@author: User
"""

# variables:
#    input -- the array of items to be sorted; key(x) returns the key for item x
#    n -- the length of the input
#    k -- a number such that all keys are in the range 0..k-1
#    count -- an array of numbers, with indexes 0..k-1, initially all zero
#    output -- an array of items, with indexes 0..n-1
#    x -- an individual input item, used within the algorithm
#    total, oldCount, i -- numbers used within the algorithm

# calculate the histogram of key frequencies:
def continue_sorting(array, m):
    
    count = {i:0 for i in range(m)}    
    for x in array:
        count[x] += 1   

    # calculate the starting index for each key:
    total = 0
    for i in range(m): 
        oldCount = count[i]
        count[i] = total
        total += oldCount
    
    # copy to output array, preserving order of inputs with equal keys:
    output = {i:0 for i in range(len(array))}
    for x in array:
        output[count[x]] = x
        count[x] += 1
    
    return output.values()

array = [2,8,4,5,10,9,7,1,11]
m = max(array) + 1
print continue_sorting(array, m)