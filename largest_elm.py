my_list = [17, 92, 18, 33, 58, 7, 33, 42]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)
