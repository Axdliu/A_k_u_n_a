# -*- coding: utf-8 -*-
"""
find_two_closest_and_sum 给一个数组，和一个target_num，求数组中最接近target_num的两个数的和

@author: User
"""

def two_close_sum(num_list, target_num):
    summary = [[i, abs(i-target_num)] for i in num_list]
    sort_list = sorted(summary, key= lambda x:x[1])           
    return sort_list[0][0]+sort_list[1][0]
    
    
num_list = (1,2,3,4,5)
target_num = 3.5
    
print two_close_sum(num_list, target_num)