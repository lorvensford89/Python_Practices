def main():
    number = get_number()
    print(f"You entered: {number}")


def get_number():
    number = int(input("Enter the number: "))
    while True:
        if number >= 0:
            return number

main()