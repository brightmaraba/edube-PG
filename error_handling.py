def read_int(prompt, min_value, max_value):
    while True:
        try:
            number = int(input(prompt))
            if number < min_value or number > max_value:
                print(
                    f"Error: The value is not within permitted range {min_value}...{max_value}"
                )
                continue
            return number
        except ValueError:
            print("Error: Wrong input")


v = read_int("Enter a number: ", 0, 100)
print(f"The numbers is: {v}")
