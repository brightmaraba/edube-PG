def life_digits(date_of_birth):
    sum = 0
    try:
        digits = [int(x) for x in str(date_of_birth)]
        for i in digits:
            sum += i
        return sum
    except BaseException as e:
        print(e)


if __name__ == "__main__":
    date_of_birth = int(input("Enter your date of birth: "))
    print(life_digits(date_of_birth))
