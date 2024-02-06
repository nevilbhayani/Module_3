# write a python function that takes two lists and returns true if thay have at least one comman member

list1=[10,20,30,40,50]
print("List1 is :- ",list1)
list2=[10,80,90,70,20,30]
print("List2 is :- ",list2)

def comman_member(a,b):
    for a in list1:
        for b in list2:
            if a == b:
                print("two list is comman item : ",a)
    else:
        print("Two list are not comman")            
comman_member(list1,list2)