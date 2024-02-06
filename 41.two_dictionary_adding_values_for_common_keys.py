# Write a Python program to combine two dictionary adding values for common keys.

from collections import Counter

def combine_dictionaries(a, b):
    combined_dict = Counter(a) + Counter(b)
    
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result_dict = combine_dictionaries(d1, d2)

print("Combined Dictionary:", result_dict)
