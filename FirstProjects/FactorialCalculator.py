#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ekomsal

Calculating factorial of the value
"""

def CalcFactorial(num : int):
    temp = 1
    if num >= 0:
        while num > 0:
            temp = num * temp
            num -= 1
    
    return temp

i_value = int(input("Please enter a value: "))
print(CalcFactorial(i_value))
