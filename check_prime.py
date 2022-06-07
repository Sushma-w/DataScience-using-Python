# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:04:32 2022

@author: sushmavasamshetty
"""
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def csum(n):
    if n==1:
        return 1
    return n+csum(n-1)
n=int(input('Enter a number'))
if prime(n):
    print('it is a prime')
else:
    print('it is not a prime')
if n%2==0:
    print('it is even no')
else:
    print('it is odd no')
if n%5==0:
    print('it is divisible by 5')
else:
    print('it is not divisible by 5')
#print(n*(n+1)/2)
print('Sum=',csum(n))

