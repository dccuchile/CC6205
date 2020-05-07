#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:09:39 2020

@author: felipe
"""


def recur_factorial(n):    
    #caso base
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


def dynamic_factorial(n):   
    table=[0 for i in range(0,n+1)]
    
    # caso base
    table[0]=1
    
    for i in range(1,len(table)):
        print(i)
        table[i]=i*table[i-1]
        
    return(table[n])