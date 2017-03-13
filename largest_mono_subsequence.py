# -*- coding: utf-8 -*-
"""
[2,10]

@author: User
"""

def mono_subsequence(cards):
    
    result = []
    for i in range(len(cards)):
        result.append([cards[i]])
        for k in range(i+1, len(cards)):
            if cards[k] > result[i][-1]:
                result[i].append(cards[k])
        
    result_max = [i for i in result if len(i)==len(max(result, key=len))]
    winner1 = max(result_max, key=sum)
            
    return winner1


cards = [2,3,4,5,6,3,2,3,10,2,3,5,8,7,6,8,9,4,5,6,7,8,9]
print mono_subsequence(cards)