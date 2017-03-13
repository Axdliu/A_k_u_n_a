# -*- coding: utf-8 -*-
"""
This function prvided a sorted list of integers without duplicates,
haystack and a value, needle, returns the index where needle could be 
inserted into haystack such that haystack remains sorted.

@author: User
"""

def get_insert_point(haystack, needle):
    mid_index = len(haystack) // 2
    mid_value = haystack[mid_index]
    if mid_index == 0:
        return 1 if needle > mid_value else 0
    if mid_value == needle:
        return mid_index
    if mid_value > needle:
        return get_insert_point(haystack[:mid_index], needle)
    else:
        return mid_index + get_insert_point(haystack[mid_index:], needle)
        
haystack = [1, 3, 5, 7, 9]

for i in range(11):
    print  i, get_insert_point(haystack, i)

