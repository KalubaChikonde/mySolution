#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:19:07 2019

@author: kalubachikonde
"""

def min_swap_num(arr):
    counter = 0
    dict1 = {}   
    
    # key = item
    # value = position of item   
    for i in range(len(arr)):
        dict1[arr[i]] = i
    
    #sorts items in dictionary in correct order
    # output is (key,value) = (item,position)
    sorted_dict = sorted(dict1.items(), key=lambda kv: kv[0])
    
    #boolean array to check whether item has been checked
    checked = [False for i in range(len(arr))]
    
    for k,v in sorted_dict:
        
        # is item in correct position
        #has it already been checked
        if k == v or checked[k]:
            continue
        #calculates length of cycle
        cycle = 0
        v = k
        
        #while we haven't checked value 
        #finds cycle and length of cycle
        while not checked[v]:
            checked[v] == True 
            v = dict1[v] #find correct position of value by moving to next node 
            cycle +=1  
        counter += cycle - 1 #when cycle is found incrtease counter
    return counter
arr = [4,2,1]
min_swap_num(arr)