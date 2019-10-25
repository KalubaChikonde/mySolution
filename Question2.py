#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:09:09 2019

@author: kalubachikonde
"""
#reverses a string
mystring = input("Enter a string: ")
for i in range(len(mystring)-1,-1,-1):
    print(mystring[i],end = "")