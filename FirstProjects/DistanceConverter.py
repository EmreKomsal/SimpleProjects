#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ekomsal

Mile to Kilometer
"""

km_to_mile = 0.612

run = 0
while run == 0:
    print("What do want to convert?")
    selection = float(input("O.Exit" + "\n" +
                          "1.Km to Mile" + "\n" + 
                          "2.Mile to Km" + "\n" + 
                          "Selection: "))
    
    if selection == 0:
        print("Exiting...")
        run = 1
    elif selection == 1:
        km = float(input("Enter your distance in km: "))
        mile = km * km_to_mile
        print("Mile: " + str(mile))
    elif selection == 2:
        mile = float(input("Enter your distance in mile: "))
        km = mile / km_to_mile
        print("Kilometer: " + str(km))    
    else:
        print("Please enter a valid value")