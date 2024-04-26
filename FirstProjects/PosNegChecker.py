#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ekomsal

Checking value is positive or negative
"""


num = int(input("Please enter your number: "))

if num == 0:
    print("0 is neither positive and negative")
elif num < 0:
    print("Negative")
elif num > 0:
    print("Positive")