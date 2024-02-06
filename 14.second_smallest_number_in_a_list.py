# Write a Python program to find the second smallest number in a list.


list1=[]
num=int(input("Enter Number :"))
for i in range(num):
    n=int(input("Enter A numbers :"))
    list1.append(n)
list1.sort()   
print(list1[1])