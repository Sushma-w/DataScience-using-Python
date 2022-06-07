# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:39:31 2022

@author: sushmavasamshetty
"""

import random
n=int(input('Roll the dice'))
c=random.choice([1,2,3,4,5,6])
if n>c:
    print('You won')
elif n<c:
    print('You lost')
else:
    while n==c:
        c=random.choice([1,2,3,4,5,6])
        if n>c:
            print('You won')
        elif n<c:
            print('You lost')
        