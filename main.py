def main():
    number = get_number()
    print(f"You entered: {number}")


def get_number():
    
    while True:
        number = int(input("Enter the number: "))
        if number >= 0:
            return number
        else:
            continue

main()