# -*- coding: utf-8 -*-
"""



"""

import operator
import math

 
def Classify(trades, new_trades, labels):
    k = 3
    result = []

    for test in new_trades:
        distances = []
        length = len(test)
        for t in range(len(trades)):
            distance = 0
            for f in range(length):
                distance += pow((trades[t][f] - test[f]), 2)
            distances.append((trades[t], labels[t], math.sqrt(distance)))
    
        distances.sort(key=operator.itemgetter(2))
        neighbors = []    
        for x in range(k):
        		neighbors.append(distances[x][1])
        
        classVotes = {}
        for x in neighbors:
        		if x in classVotes:
        			classVotes[x] += 1
        		else:
        			classVotes[x] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
         
        result.append(sortedVotes[0][0])
    
    return result

trades = [[99.0, 5.0, 20.0], 
          [95.0, 15.0, 10.0],
          [5.0, 80.0, 40.0],
          [3.0, 92.0, 20.0],
]

labels = ['green', 'green','red', 'red']

new_trades = [[90.0, 10.0, 15.0], [10.0, 98.0, 50.0]]


print Classify(trades, new_trades, labels)