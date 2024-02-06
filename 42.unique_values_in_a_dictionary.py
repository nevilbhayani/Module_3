# Write a Python program to print all unique values in a dictionary\

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 200, 'e': 100}

unique = set(my_dict.values())

print("Unique Values in the Dictionary:", unique)