# -*- coding: utf-8 -*-
"""
L for a-z
U for A-Z
D for 0-9

@author: User
"""

import string
import itertools

string_1 = 'zZ1_example_aA1bB2c'  
# "LUD" returns "aA1bB2"

L = string.lowercase[:]
U = string.uppercase[:]
D = string.digits

pattern = 'LUD'
unit = [eval(k) for k in pattern]
        
result = []

for i in range(len(string_1)):
    codebook = itertools.cycle(unit)
    counter = 0
    for n in string_1[i:]:
        match = next(codebook)
        if n in match:
            counter += 1
        else:
            break
    if counter != 0:
        result.append(string_1[i:i+counter-(counter%len(pattern))])
        
print max(result, key=len)

        
    
            
        
        
        