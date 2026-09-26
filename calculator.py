def main():
    print("Enter two numbers:")
    a = int(input("a = "))
    b = int(input("b = "))

    # square of each number
    print(f"Square of {a}: {square(a)}")
    print(f"Square of {b}: {square(b)}")

    # add the two numbers
    print(f"{a} + {b} = {add_two_nbs(a, b)}")

def square(a):
    result = a * a
    return result

def add_two_nbs(a, b):
    result = a + b
    return result


main()





