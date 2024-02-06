#  Write a Python program to replace last value of tuples in a list

list=[(1,2,3),(4,5,6),(7,8,9)]
for x in range(len(list)):
    list[x]=list[x][:-1]+("nevil",)
print(list)