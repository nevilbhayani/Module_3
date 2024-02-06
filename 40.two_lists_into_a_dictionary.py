# Write a Python program to map two lists into a dictionar

def fun1(l1):
       return l1**3 
list1=[1,2,3,4,5,6,7,8,9,10]
data=map(fun1,list1)  
for i in data:
    print(i,end=" ")