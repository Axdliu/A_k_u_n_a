# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 15:15:25 2017

@author: User
"""

import string

def convert_to_sum(word):
    set_full = list(string.lowercase[:] + string.uppercase[:])
    value_full = range(1,27)*2
    book = dict(zip(set_full, value_full))
    return sum(book[letter] for letter in word)
    
test = 'TEST'
print convert_to_sum(test)