def main():

    while True:
        try:
            guess = guessing_number()
            break
        except ValueError as e:
            print(f"Invalid: {e}.Try again.")



def guessing_number():
    number = int(input("Enter the guessed number: "))
    if not 1 <= number <= 100:
        raise ValueError("Out of range!")   # detection of crashing
    return number


if __name__ == "__main__":
    main()