#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:09:39 2020

@author: felipe
"""

# more info https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/improving-efficiency-of-recursive-functions


# fac(0)=1 fac(n)=n*fac(n-1)

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
        table[i]=i*table[i-1]
        
    return(table[n])

# Fibbonnacci
#f(0)=f(1)=1, f(n) = f(n-1) + f(n-2).

def recur_fibbonacci(n):
    if n == 1 or n==0:
        return 1
    else:
        return recur_fibbonacci(n-1)+recur_fibbonacci(n-2)
    
    
# Complejidad exponencial
    
    
def dynamic_fibbonacci(n):   
    table=[0 for i in range(0,n+1)]
    
    # caso base
    table[0]=1
    table[1]=1
    
    for i in range(2,len(table)):
        table[i]=table[i-1]+table[i-2]
        
    return(table[n])

# Complejidad lineal