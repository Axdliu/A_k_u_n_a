# -*- coding: utf-8 -*-
"""
能不能把一个数分解成3个正整数相乘（不包括1）

@author: User
"""

def three_product(int_number):
    
    result = []

    def breakdown(int_number):
        if int_number > 1:
            for i in range(3, int_number+1):
                if int_number%i == 0:
                    result.append(i)
                    breakdown(int_number//i)
                    break
                    
    breakdown(int_number)
               
    print result            
    if len(result) >= 3:
        return "Yes"
    else:
        return "No"

        
int_number = 345
print three_product(int_number)    
        