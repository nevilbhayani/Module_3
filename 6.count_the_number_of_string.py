# Write a python program to count the number of string where the string length is 2 or more andv the first and last charactar are same from a givan list of strings

def generate_square_list():
    square_list = [i**2 for i in range(1, 31)]

    print("First 5 elements:", square_list[:5])

    print("Last 5 elements:", square_list[-5:])

if __name__ == "__main__":
    generate_square_list()