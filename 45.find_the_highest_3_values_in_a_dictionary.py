# Write a Python program to find the highest 3 values in a dictionary

dict1={'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69 , 'G':82}
list1=list(dict1.values())  
list1.sort(reverse=True)
print(list1[:3])