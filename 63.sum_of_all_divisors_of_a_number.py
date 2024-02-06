# Write a Python program to returns sum of all divisors of a number

def sum_div(num):
    divisors = [1]      
    for i in range(1, num):
        if (num % i)==0: 
            print(i)   
            divisors.append(i)
    return sum(divisors)

num=int(input("Enter num :"))
print("sum of all divisors num :-",sum_div(num)-1)