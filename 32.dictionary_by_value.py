# Write a Python script to sort (ascending and descending) a dictionary by value

dict1={'a': 4, 'b': 6, 'c': 2, 'd': 5, 'e': 1, 'f': 3}
list1=list(dict1.keys())   
list1.sort()     
dict2={}     
for i in list1:
    dict2.update({i:dict1[i]})   
    
print("ascending dict",dict2) 
print("")
list1=list(dict1.keys())  
list1.sort(reverse=True)     
dict2={}
for i in list1:
    dict2.update({i:dict1[i]}) 
    
print("descending dict",dict2)  