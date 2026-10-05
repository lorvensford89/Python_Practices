def main():
    lines(1)

    number = get_integer()
    print(f"{number}")

    lines(2)
    square("x", 4, 4)
    lines(2)

    try:
        print(f"{division(12, 4):.0f}")
    except ZeroDivisionError as error:
        print(f"{error}")
    else:
        print("Division was done successfully")
    finally:
        print("The check with exception went good.")

    lines(2)

    dictionary_check()

    lines(2)


    

def square(symbol, length, width):
    for i in range(length):
        for j in range(width):
            print(symbol, end="")
        lines(1)


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    else:
        result = a / b
        return result


def get_integer():
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            pass
        else:
            return number


def dictionary_check():
    El_info = {
        "Name": "EL",
        "Age": 22,
        "Profession": "Software Engineer"
    }

    for key, value in El_info.items():
        print(f"{key}: {value}")



def lines(a):
    for i in range(a):
        print("")



if __name__ == "__main__":
    main()