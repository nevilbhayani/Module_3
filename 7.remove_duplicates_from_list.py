# Write a Python program to remove duplicates from a list.

list=[10,20,20,30,40,40,40,50,]
print("Orignal lis is :- ",list)

list1 = [] 
for i in list:   
    if i not in list1: 
        list1.append(i)  
print("List After removing duplicates ", list1)