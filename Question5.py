#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:45:27 2019

@author: kalubachikonde
"""

#Given an array of integers nums and an integer k
#determine whether there are two distinct indices i and j in the array where nums[i] = nums[j]
#and the absolute difference between i and j is less than or equal to k
def containsCloseNums(nums,k):
    for i in range(0,len(nums)+1):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                if (abs(i-j) <= k):
                  print("True")
                else:
                  print("False")
nums = [0,1,2,3,5,2]
k = 3
containsCloseNums(nums,k)
