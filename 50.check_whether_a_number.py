#  Write a Python function to check whether a number is perfect or not.


def is_perfect_number(number):
    if number <= 0:
        return False 

    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    return divisors_sum == number

num_to_check = 28  

if is_perfect_number(num_to_check):
    print(f"{num_to_check} is a perfect number.")
else:
    print(f"{num_to_check} is not a perfect number.")
