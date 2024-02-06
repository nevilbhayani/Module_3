# Write a Python program to check whether a list contains a sub list

list=[10,['nevil',2.33],[3.33,5,6],['python',"5 :hallo"]]

print("orignal list=",list)  
for i in list:
    if len(list) > 1:
        print("sublist is present in list")
        break 
    else:
        print("sub list is present not in list")