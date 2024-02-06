# Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(input_str):
    clean_str = ''.join(char.lower() for char in input_str if char.isalnum())

    return clean_str == clean_str[::-1]

# Example usage:
word_to_check = "A man, a plan, a canal: Panama"  

if is_palindrome(word_to_check):
    print(f'"{word_to_check}" is a palindrome.')
else:
    print(f'"{word_to_check}" is not a palindrome.')
