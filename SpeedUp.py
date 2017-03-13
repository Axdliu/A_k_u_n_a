# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 22:36:12 2017

@author: User
"""

class AverageCalculator:
    
    def __init__(self, sequence):
        self.seq = sequence
        self.items = [x for x in sequence]

    def get_avg(self):
        count = 0.0
        for i in self.items:
            count += i
        return (float(count) / len(self.items))


class AverageCalculator2:
    
    def __init__(self, sequence):
        self.seq = sequence
    
    def get_avg(self):
        return sum(self.seq, 0.0) / len(self.seq)

        
iterable1 = range(1000000)
iterable2 = range(10000000)
   
import time
start_time = time.time()
test1 = AverageCalculator(iterable1)
print test1.get_avg()
print("--- %s seconds ---" % (time.time() - start_time))


import sys
import os
import itertools
    
start_time = time.time()    
test2 = AverageCalculator2(iterable2)
print test2.get_avg()
print("--- %s seconds ---" % (time.time() - start_time))