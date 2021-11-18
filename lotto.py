draw = [3, 7, 11, 42, 34, 49]
result = [5, 11, 8, 42, 3, 49]

count = 0
for number in result:
    if number in draw:
        count += 1

print(f"You hit {count} numbers in the draw")
