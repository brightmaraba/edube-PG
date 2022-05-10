def is_palindrome(strng):
    """
    Checks if a string is a palindrome.
    """
    if strng == strng[::-1]:
        return "It is a palindrome."
    else:
        return "It is not a palindrome."


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print(is_palindrome(input_string))
