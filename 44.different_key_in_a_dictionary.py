# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd


dict1= {'1':['a', 'b'], '2':['c', 'd']}
list1= list(dict1.values())  
for i in list1[0]:   
    for j in list1[1]:    
        print(i+j,end=" ")