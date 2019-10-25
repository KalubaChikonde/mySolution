#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:07:05 2019

@author: kalubachikonde
"""
#Write a program that prints the numbers from 1 to 100.
# But for multiples of three print 'Fizz' instead of the number 
#for the multiples of five print 'Buzz'. 
#For numbers which are multiples of both three and five print 'FizzBuzz'
def multiples():
    for i in range(1,101):
        if ((i%3) == 0 and (i%5) == 0):
            print("FizzBuzz")
        elif (i%5) == 0:
            print("Buzz")
        elif (i%3) == 0:
            print("Fizz")
        else:
            print(i)
          
multiples()
