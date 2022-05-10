# Create a seven-segment display using a string of characters.
# A '#' represents a segment/LED.
# Step 1: Create a string of characters that represents the seven-segment display.
# Step 2: Use a for loop to iterate through the string.


print0 = ("###", "# #", "# #", "# #", "###")
print1 = ("  #", "  #", "  #", "  #", "  #")
print2 = ("###", "  #", "###", "#  ", "###")
print3 = ("###", "  #", "###", "  #", "###")
print4 = ("# #", "# #", "###", "  #", "  #")
print5 = ("###", "#  ", "###", "  #", "###")
print6 = ("###", "#  ", "###", "# #", "###")
print7 = ("###", "  #", "  #", "  #", "  #")
print8 = ("###", "# #", "###", "# #", "###")
print9 = ("###", "# #", "###", "  #", "###")

print_list = [
    print0,
    print1,
    print2,
    print3,
    print4,
    print5,
    print6,
    print7,
    print8,
    print9,
]

try:
    input_integer = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
    exit()

input_string = str(input_integer)
input_digits = [int(x) for x in input_string]

for i in range(5):
    result = ""
    for j in input_digits:
        result += print_list[j][i] + " "
    print(result, sep="\n")
