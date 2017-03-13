# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 00:04:47 2017

@author: User
"""

def pddate_num(year):
    
    century = range(year//1000*1000+1, year//1000*1000+101)
    counter = 0
            
    calendar1 = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
    calendar2 = calendar1
    calendar2['02'] = 29

    for year in century:
        
        if year % 400 == 0:
            calendar = calendar2
        elif year % 100 == 0:
            calendar = calendar1
        elif year % 4 == 0:
            calendar = calendar2
        else:
            calendar = calendar1
                 
        revert_year = str(year)[::-1]
        if revert_year[0:2] in calendar.keys():
            if int(revert_year[2:4]) <= calendar[revert_year[2:4]] and int(revert_year[2:4]) != 0:
                counter += 1
                
        if '0'+ revert_year[0] in calendar.keys():
            if int(revert_year[1:3]) <= calendar['0'+ revert_year[0]]  and int(revert_year[1:3]) != 0:
                counter += 1
            
    return counter
   
print pddate_num(2016)