#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:18:37 2019

@author: kalubachikonde
"""

#function that computes the list of the first n Fibonacci numbers
def fibonacci(n): 
    seq = []        
    curr = 0
    nxt = 1
    i = 0
    while (i < n):
        seq.append(curr)
        sum_ = curr + nxt
        curr = nxt
        nxt = sum_
        i +=1
    print(seq)
#computes the first 100 Fibonacci numbers
fibonacci(100)

    
    