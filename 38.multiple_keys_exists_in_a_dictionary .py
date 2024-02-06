#  Write a Python program to check multiple keys exists in a dictionary


def key(a, b):
   
    return all(key in a for key in b)


a = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

b = ['apple', 'orange', 'kiwi']

result = key(a, b)

if result:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")