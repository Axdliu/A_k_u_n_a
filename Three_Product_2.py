# -*- coding: utf-8 -*-
"""
其实意思就是array_size 是否是三个整数比2大的整数的乘积

@author: User
"""

def three_product(int_number):
    
    result = []

    for i in range(3, int_number):
        if int_number%i == 0:
            result.append(i)
               
    print result            
    if len(result) >= 3:
        return "Yes"
    else:
        return "No"

        
int_number = 345
print three_product(int_number)    
        