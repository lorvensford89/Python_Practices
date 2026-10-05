"""
Implement a program that prompts the user for the name of a variable
in camel case and outputs the corresponding name in snake case.
Assuming that the user's input will indeed be in camel case.
"""

def main():
    user_input = input("camelCase: ")
    print("snake_case: ", end="")

    # The loop for each letter in user_input
    for c in user_input:
        # Asking if each of character in user_input is upper case
        if c.isupper():
            # Print "_" plus lowercase letter without newline
            print("_" + c.lower(), end="")
        else:
            # Print the same character without newline
            print(c, end="")

    print()

main()