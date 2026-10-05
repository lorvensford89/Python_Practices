def main():
    text = "4/3"
    parts = text.split("/")


    print(parts)    # Variable 'parts' becomes a list

    a = int(parts[0])
    b = int(parts[1])

    print(a, b)

    lines(2)
    problem_set3()
    lines(2)


"""
In a file called fuel.py, implement a program that prompts the user for a
fraction, formatted as X/Y, wherein X is a non-negative integer and Y 
is a positive integer, and then outputs, as a percentage rounded to the
nearest integer, how much fuel is in the tank. If, though, 1% or less 
remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank 
is essentially full.
"""

def problem_set3():
    # TODO: separate the input and assign interger value to variables

    while True:
        try:
            user_input = input("Fractions: ")
            parts = user_input.split("/")
            x = int(parts[0])
            y = int(parts[1])
            if x < 0 or y <= 0:     # No need for multiple exceptions
                continue            # if y = 0, the loop will start again
        except ValueError:
            pass
        else:                   
            result = (x/y) * 100
            if result <= 1:         # Condions for correct display
                print("E")
            elif result >= 99:
                print("F")
            else:
                print(f"{round(result)}%")
            break

    # TODO: Implement the conditions for the correct display (E/F)



def lines(a):
    for i in range(a):
        print("")



if __name__ == "__main__":
    main()