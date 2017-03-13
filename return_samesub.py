# -*- coding: utf-8 -*-
"""
给两个string，求相同的character，character可以有duplicate，举例 s1 = aabccc, s2 = abcc, return abcc 


@author: User
"""

str1 = 'aabccca'
str2 = 'abccaabccca'

def samesub(str1, str2):
    
    answer = ""
    len1, len2 = len(str1), len(str2)
    for i in range(len1):
        if len1 - i > len(answer):
            match = ""
            counter = 0
            for j in range(len2):
                if counter <= len1 - i -1 and str1[i + counter] == str2[j]:
                    match += str2[j]
                    counter += 1
                else:
                    if (len(match) > len(answer)): 
                        answer = match
                    match = ""
                    counter = 0  
                if (len(match) > len(answer)): 
                    answer = match
        
    return answer
     
print samesub(str1, str2)