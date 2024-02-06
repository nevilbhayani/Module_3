# Write a Python script to merge two Python dictionaries


dict1 = {"nevil":10,"raj":20}
dict2 = {"meet":30,"krish":40}
dict3={}   

for i in (dict1,dict2):
    dict3.update(i)
print(dict3)   