# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 00:29:30 2017

@author: User
"""
import re

def remove_char(string, char):
    return re.sub(char, '', string)
    
print remove_char('fegsig', 'g')