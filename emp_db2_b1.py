emp_data={}
for i in range(2):
    id1=int(input('enter student '+str(i+1)+' id\n'))
    name=input('enter student '+str(i+1)+' name\n')
    sal=float(input('enter student '+str(i+1)+' salary\n'))
    des=input('enter student '+str(i+1)+' designation\n')
    emp_data['std-'+str(i+1)]={'emp_id':id1,'emp_name':name,'emp_sal':sal,'emp_des':des}
print(emp_data)