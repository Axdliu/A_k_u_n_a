# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 15:00:45 2017

@author: User
"""


list1 = [2,8,9,9]


def max_product(list1):
    max_prod = 0
    while list1 != []:
        back = list1.pop()
        for i in list1:
            if i < back and i*back >= max_prod:
                max_prod = i*back
    return max_prod
    
print max_product(list1)
        
