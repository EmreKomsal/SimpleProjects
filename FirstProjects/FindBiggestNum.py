#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ekomsal

Find biggest number in list
"""

num_list = []

valid = False

while valid == False: 

    num_count = int(input("Please enter your number count: "))

    if num_count <= 0:
        print("Please enter valid value...")
    else:
        valid = True
    
i = 0

while i < num_count:
    num_list.append(int(input("Please enter your " + str(i + 1) + " value: ")))
    i += 1
    
num_list.sort(reverse= True)

print("Biggest number is: " + str(num_list[0]))