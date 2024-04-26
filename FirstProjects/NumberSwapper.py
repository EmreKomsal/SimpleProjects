#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ekomsal

This a code block for swapping to variables without using 3rd variable

General Method
"""

x = 10
y = 20

print("X:" + str(x)) #10
print("Y:" + str(y)) #20
print("")

x = x + y #30
y = x - y #30 - 10 = 20
x = x - y #30 - 20 = 10

print("X:" + str(x)) #20
print("Y:" + str(y)) #10
print("")

"""

Python method

"""

x,y = y,x # 20,10 = 10,20

print("X:" + str(x))
print("Y:" + str(y))
print("")