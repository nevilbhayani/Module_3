# Write a python program to ganerate and print a list of first and last 5 elements where the values are square of numbers beetween 1 and 30


list=[]  
for i in range(1,31): 
    print(i)
    list.append(i**2)

print("\nFirst 5 elements:", list[:5])
print("Last 5 elements:", list[-5:])