# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    if not numbers:
        return None, None  

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum


num = [3.14, 2.718, 1.414, 0.0, -1.0, -2.5]
max_value, min_value = find_max_min(num)

print("Maximum value:", max_value)
print("Minimum value:", min_value)