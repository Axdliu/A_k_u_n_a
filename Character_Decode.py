# -*- coding: utf-8 -*-
"""
fefe
"""

import string

def Char_decode(string_key, str_1):
    codebook = dict(zip(string.lowercase[:], string_key))
    decoded = ''
    for l in str_1:
        if int(codebook[l])%3 != 0:
            decoded += l
    return decoded

string_key = '00001002336469700000000369'
str_1 = 'amhbcdeplklsczo'
print Char_decode(string_key, str_1)