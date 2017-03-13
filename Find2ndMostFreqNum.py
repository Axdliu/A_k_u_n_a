# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 00:43:59 2016

@author: User
"""


list_1 = [0, 1, 2, 2, 2, 2, 1, 0, 5, 1]

def Second_mostFreq(list_1):

    set_1 = set(list_1)
    dict_1 = dict((k,1) for k in set_1)
    
    for i in set_1:
        dict_1[i] = list_1.count(i)
    
    dict_sorted = sorted(dict_1.items(), key=lambda x: x[1], reverse=2)
    
    return dict_sorted[1][0]

print Second_mostFreq(list_1)
