def main():
    lines(1)

    square("x")
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


    

def square(symbol):
    for i in range(4):
        for j in range(4):
            print(symbol, end="")
        lines(1)


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    else:
        result = a / b
        return result


def lines(a):
    for i in range(a):
        print("")



if __name__ == "__main__":
    main()