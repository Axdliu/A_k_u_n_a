# -*- coding: utf-8 -*-
"""
给一个vector和int n，除掉vector里面出现n次的元素，并返回升序排列的结果。

@author: User
"""

def n_remover(vec, n):
    summary = {i:0 for i in set(vec)}
    for i in vec:
        summary[i] += 1
    result = []
    for i in set(vec):
        if summary[i] != n:
            result.append(i)
    return sorted(result)
    
    
vec = ['fe', 'f', 'aw1', 'te', 'iu', 'te', 'te']
n = 3

print n_remover(vec, n)