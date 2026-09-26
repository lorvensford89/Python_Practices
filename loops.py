def main():
    print(get_number())

def get_number():
    while True:
        number = int(input("Enter a number: "))
        if number > 0:
            return number

main()
