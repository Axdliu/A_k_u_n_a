# -*- coding: utf-8 -*-
"""
hashable objects?

only tuple and string are hashable here

There are currently two builtin set types, set and frozenset. 
The set type is mutable -- the contents can be changed using methods like add() and remove(). 
Since it is mutable, it has no hash value and cannot be used as either a dictionary key 
or as an element of another set. 

The frozenset type is immutable and hashable --
 its contents cannot be altered after is created; however, 
 it can be used as a dictionary key or as an element of another set.

@author: User
"""

A = {1:2, 3:4}
B = [1,2,3,4]

C = (1,2,3,4)
D = {1,2,3,4}
E = "1,2,3,4"

