# >Write a Python program to select an item randomly from a list. 


def split_list(input_list):
    if len(input_list) < 3:
        print("List should have at least three elements for splitting.")
        return

    first_element, second_element, *remaining_elements = input_list

    print("First element:", first_element)
    print("Second element:", second_element)
    print("Remaining elements:", remaining_elements)

my_list = [1, 2, 3, 4, 5, 6]
split_list(my_list)