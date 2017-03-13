# -*- coding: utf-8 -*-
"""
@author: User
"""

seq1 = [8, -1, 6, 7, 2, 18, -12]
seq2 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

seq = seq2
select = [[]]
n = 0
select[n].append(seq[0])

for i in range(1, len(seq)):
    temp = seq[i-1]
    if seq[i] - temp == 1:
        select[n].append(seq[i])
    else:
        select.append([seq[i]])
        n += 1

print max(select, key=len)