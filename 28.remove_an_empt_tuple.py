#  Write a Python program to remove an empty tuple(s) from a list of tuples.

list1=[(10,20),("hello","World"),(25,"Rakshit"),(  ),(25,26)]
print("orignel list :",list1)
for i in list1:
    if(len(i)==0):  
        list1.remove(i) 
print(list1)