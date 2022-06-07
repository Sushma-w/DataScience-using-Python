# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:36:01 2022

@author: sushmavasamshetty
"""
emp_data={}
for i in range(2):
    id1=int(input('enter student '+str(i+1)+' id\n'))
    name=input('enter student '+str(i+1)+' name\n')
    sal=float(input('enter student '+str(i+1)+' salary\n'))
    des=input('enter student '+str(i+1)+' designation\n')
    emp_data['std-'+str(i+1)]=[id1,name,sal,des]
#print(emp_data) 
for std,std_info in emp_data.items():
    print(std,'-',std_info)
    