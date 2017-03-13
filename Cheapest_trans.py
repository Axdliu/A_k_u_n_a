# -*- coding: utf-8 -*-
"""
maximum of three transforms

@author: User
"""

def cost_function(start, end):
    '''    
    costs = {#    a  b  c  d  e  f
             'a':[0, 6, 9, 1, 5, 9],
             'b':[2, 0, 1, 6, 9, 6],
             'c':[6, 6, 0, 2, 7, 4],
             'd':[6, 4, 7, 0, 4, 3],
             'e':[1, 3, 5, 4, 0, 7],
             'f':[9, 4, 5, 9, 2, 0]}
    '''
    costs = {#    a  b  c 
             'a':[0, 3, 2],
             'b':[5, 0, 2],
             'c':[1, 6, 0]}
    key = sorted(costs.keys(), key=lambda x:x[0])
    return costs[start][key.index(end)]
         
input_list = ('c', 'b')
maps = 'abc'

print cost_function(input_list[0], input_list[1])

def min_transform(input_list):
    cost = cost_function(input_list[0], input_list[1])
    path = list(input_list)
    for i in maps:
        for j in maps:
            cost_temp = cost_function(input_list[0], i) + cost_function(i, j) + cost_function(j, input_list[1])
            if cost_temp < cost:
                cost = cost_temp
                path = [input_list[0], i, j, input_list[1]]
    
    print path    
    return cost 
    
print min_transform(input_list)