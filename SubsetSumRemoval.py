# -*- coding: utf-8 -*-
"""
@author: User
"""

import itertools

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def subsetsum(setr):
    if len(setr) <= 1:
        return
    for i in setr:
        temp_set = setr[:]
        temp_set.remove(i)
        for n in range(1, len(temp_set)):
            x = itertools.combinations(temp_set, n)
            while True:
                try:
                    group = next(x)
                    if sum(group) == i:
                        for k in group:
                            setr.remove(k)
                        setr.remove(i)
                        subsetsum(setr)
                except:
                        break


set1 = [1, 3, 5, 6]
set2 = [48, 20, 1, 3, 4, 6, 9, 24, 789, 8909]

setr = set2
setr.sort(reverse=2)

subsetsum(setr)                   
                    
print '\nThe result is: \n', setr, len(setr)


