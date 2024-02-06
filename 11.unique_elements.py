# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(list1):
    list1=set(list1)
    set1=list(list1)
    print(set1)

list1=[10,20,30,40,10,20,60,40,90,10]

unique(list1)
