# User enters a message and the program encrypts it using a caeser cipher.
# The program will ask the user for the shift value.
# The shift value will be a number between 0 and 25.
# Numbers will not be shifted.
def caesers_cipher(input_message, shift_key):
    output_cipher = ""
    for char in input_message:
        if char.isalpha() == True:
            output_cipher += chr(ord(char) + shift_key)
        else:
            output_cipher += char
    return output_cipher


print(caesers_cipher("Hello World! 123", 24))
