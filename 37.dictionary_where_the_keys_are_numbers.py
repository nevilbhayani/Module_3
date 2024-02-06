# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

dict = {num: num**2 for num in range(1, 16)}

print("Dictionary with keys as numbers between 1 and 15:")
print(dict)