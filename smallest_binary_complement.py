# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 12:05:51 2017

@author: User
"""

def min_binaryC(num):
    binary = str(format(num, "08b"))
    min_binary = str(int(binary,10))
    binaryC = ''.join([str(1-int(i)) for i in min_binary])
    return int(binaryC,2)
    
num = 13
print min_binaryC(num)