# This is a calculator program

import math

def main():

    print("===== Calculator =====", end="")
    lines(2)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square root", end="")
    lines(2)
    print("=======================", end="")
    lines(3)

    logic()

    lines(3)


# Getting valid choice of operation
def valid_choice():
    number = int(input("Pick an operation >> "))
    if not 1 <= number <= 6: 
        raise ValueError("Invalid operation!")
    return number

# Getting valid numbers for operating
def getting_numbers():
    while True:
        try:
            number = float(input("Number: "))
        except ValueError:
            print("Invalid number!")
            continue
        else:
            return number

# Implementation of the calculator logic
def logic():
    # TODO
    operations = ["Addition", "Substraction", "Multiplication", "Division", "Square", "Square root"]

    lines(2)

    # Taking valid input
    try:
        choice = valid_choice()
    except ValueError as error:
        print(f"Error: {error}")
    else:
        for i in range(len(operations)):
            print(f"{choice}. {operations[choice - 1]}")
            break

        lines(2)

        match choice:

            # Addition
            case 1: 
                number1 = getting_numbers()
                number2 = getting_numbers()
                sum = number1 + number2
                print(f"Sum = {sum:.2f}", end="")

            # Substraction
            case 2:
                number1 = getting_numbers()
                number2 = getting_numbers()
                difference = number1 - number2
                print(f"Difference = {difference:.2f}", end="")

            # Multiplication
            case 3: 
                number1 = getting_numbers()
                number2 = getting_numbers()
                product = number1 * number2
                print(f"Product = {product:.2f}", end="")

            # Division
            case 4:
                number1 = getting_numbers()
                try:
                    number2 = getting_numbers()
                    if number2 == 0:
                        raise ZeroDivisionError("Division by zero.")
                except ZeroDivisionError as error:
                    print(f"Error: {error}")
                else:
                    quotient = number1 / number2
                    print(f"Quotien = {quotient:.2f}", end="")

            # Square
            case 5:
                number = getting_numbers()
                square = pow(number, 2)
                print(f"Square = {square:.2f}", end="")

            # Square root
            case 6:
                try:
                    number = getting_numbers()
                    if number < 0:
                        raise ValueError("Square root negative numbers.")
                except ValueError as error:
                    print(f"Error: {error}")
                else:
                    square_root = math.sqrt(number)
                    print(f"Square root = {square_root:.2f}")
            



def lines(a):
    for i in range(a):
        print("")


if __name__ == "__main__":
    main()



