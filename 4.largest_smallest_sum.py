# Write a python function to get the largest number,smallest num and sum of all from a list.

def number(a):
    print("Lar num :",max(list))
    print("Lar num :",min(list))
    sum=0
    for i in list:
        sum+=i
    print("Sum ans :",sum)


list=[]
n=int(input("Enter Elements :"))
for i in range(n):
    list.append(int(input("value :")))
print("list is =",list)
number(list)