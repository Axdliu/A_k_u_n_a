# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 22:45:40 2017

@author: User
"""

def  StairCase(n):
    for i in range(n):
        print ' '*(n-i) + '#'*(i+1)
        
n = 6
StairCase(n)