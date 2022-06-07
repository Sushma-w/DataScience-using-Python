# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:49:03 2022

@author: sushmavasamshetty
"""

annual=int(input('Enter annual income\n'))
hra=int(input('Enter hra\n'))*12
others=int(input('Enter other deductions (<80000)\n'))
total=annual-hra-others
print(total)
tax=0
if total<=300000:
    print(tax)
elif total>300000 and total<=600000:
    tax=total*0.1
    print(tax)
elif total>600000 and total<=1000000:
    tax=total*(15/100)
    print(tax)
else:
    tax=total*0.2
    print(tax)