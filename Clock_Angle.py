# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 00:17:24 2017

@author: User
"""


def clock_angle(hour, minute):
    hour_angle = (hour + minute*1.0/60)/12*360
    minute_angle = minute*1.0/60*360
    angle = abs(hour_angle - minute_angle)
    if angle > 180 :
        angle = 360 -angle
    return angle
    
print clock_angle(12, 24)