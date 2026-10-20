

def main():
    number = int(input("Enter a number: "))
    print(f"Square of {number}: {square(number)}")



def square(number):
    return pow(number, 2)


if __name__ == "__main__":
    main()