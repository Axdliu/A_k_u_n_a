# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 02:06:58 2017

@author: User
"""


def delivery_time(seq):
    
    seq_list = []
    for step in seq:
        for i in range(len(step)):
            if step[i] == '-' :
                seq_list.append([step[:i], int(step[i+1:])])
    
    drones = tuple(set(i[0] for i in seq_list))    
    summary = { i:[] for i in drones}
    for i in seq_list:
        summary[i[0]].append(i[1])
    drones_map = { i:1 for i in drones}
    
    print drones_map
    print seq_list
    print drones
    print summary
    counter = 0
    while seq_list != []:
        counter += 1
        for drone in drones:
            if drone == seq_list[0][0]:
                if drones_map[drone] == summary[drone][0]:
                    summary[drone].pop(0)
                    seq_list.pop(0)
                    break
                elif drones_map[drone] < summary[drone][0]:
                    drones_map[drone] +=1
            elif summary[drone] != []: 
                if drones_map[drone] < summary[drone][0]:
                    drones_map[drone] +=1
        # print counter, drones_map, seq_list

    return counter

seq = ['1234-1', '1235-1', '1235-3', '1234-2']
print delivery_time(seq)
