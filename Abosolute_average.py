# -*- coding: utf-8 -*-
"""
floor division floor(x) = [x] is the largest
integer less than or equal to x

@author: User
"""


def floor(list_1):
    return abs(sum(list_1)//len(list_1))

list_1 = [1,-2,3,4,-5,-6]
print floor(list_1)