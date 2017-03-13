# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 16:22:13 2017

@author: User
"""

def get_avg_and_sum(input_list):
    new_list = [i for i in input_list if input_list.index(i)%2 == 0]
    return sum(new_list), sum(new_list)//len(new_list)
    
total, avg = get_avg_and_sum([1,2,3])
print total, avg