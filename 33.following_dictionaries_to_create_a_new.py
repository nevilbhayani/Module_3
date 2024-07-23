# Write a Python script to concatenate following dictionaries to create a new one

dict1={'brand':'apple','nevil':10,'model': 'Mustang'}
dict2={'python':1,"year": 1964}

dict3={}  
for i in (dict1,dict2):   
        dict3.update(i)  
print("concatenate dict",dict3)



