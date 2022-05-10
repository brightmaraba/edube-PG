try:
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    # Remove spaces from both strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    # Change all letters to upper case
    str1 = str1.upper()
    str2 = str2.upper()
    # Convert both strings to lists
    str1 = list(str1)
    str2 = list(str2)
    # Sort both lists
    str1.sort()
    str2.sort()
    # Convert both lists to strings
    str1 = "".join(str1)
    str2 = "".join(str2)
    # Check if both strings are equal
    if str1 == str2:
        print("ANAGRAM!")
    else:
        print("NOT ANAGRAM!")
except BaseException as e:
    print(e)
