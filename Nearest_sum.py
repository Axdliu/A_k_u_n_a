# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 22:57:33 2017

@author: User
"""

list1 = [1,3,4,5,6,7,6,6,3]
n = 39

def nearest_sum(list1, n):
    value = sum(list1)
    answer = (0, len(list1)-1)
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if abs(sum(list1[i:j+1]) - n) < abs(value - n):
                value = sum(list1[i:j+1])
                answer = (i, j)
            elif abs(sum(list1[i:j+1]) - n) == abs(value - n):
                if i < answer[0]:
                    answer = (i, j)
                elif i == answer[0]:
                    if j < answer[1]:
                        answer = (i, j)
    return answer

print nearest_sum(list1, n)