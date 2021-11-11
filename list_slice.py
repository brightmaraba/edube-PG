import random
# List slicing
# Syntax: list_b = list_a[start_index:end_index-1]
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1[1:5]

print(list_2)


# Negative indexing
list_3 = [1, 2, 3, 4, 5]
list_4 = list_3[1:-1]  # [2, 3, 4] -> Means start from index 1 and end at index -1

print(list_4)

# Omitting the start index and end index
list_5 = [1, 2, 3, 4, 5]
list_6 = list_5[:4]  # Means start from index 0 to 3
list_7 = list_5[2:]  # Means start from index 2 to end

print(list_6)
print(list_7)

# Omitting the start index and end index
list_8 = [1, 2, 3, 4, 5]
list_9 = list_8[:]  # Means start from index 0 to end

print(list_9)

# The in and not in operators
# Syntax: in_operator = element in list
list_10 = [1, 2, 3, 4, 5]
print(1 in list_10) # True if element is in list, False Otherwise
# Syntax: not_in_operator = element not in list
print(1 not in list_10) # True if element is not in list, False Otherwise

list_11 = [random.randrange(1, 100, 2) for i in range(10)]
print(list_11)
