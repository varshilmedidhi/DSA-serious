#integers  
num1=11 # if you create a integer in memory then you can't change it 
num2=num1 # if you point a variable to another and change any of them , the other doesn't get effected
num1=22
print(num2 )
#integers are immutable so cant be change



#Dictionary 
dict1={'value':1}
dict2=dict1
dict1['value']=2 #but when you point one dict to another  and change the any dict (in this case dict1 ) then dict2 also changes.
print(dict1,dict2)

