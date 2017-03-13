# -*- coding: utf-8 -*-
"""
word_distance 给一个字符串中，给两个word，和一个数字n，
求这两个word在字符串中距离(<=n)的情形有多少组

@author: User
"""

import re

word = 'TARGET'

string = 'asdhfhhuwuTARGETdfsjefeijiTARGETGOALfe'

match = [m.start() for m in re.finditer(word, string)] 

print match