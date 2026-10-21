
def main():
    """
    In a file called bank.py, implement a program that prompts the user
    for a greeting. If the greeting starts with “hello”, output $0. If the
    greeting starts with an “h” (but not “hello”), output $20. Otherwise,
    output $100. Ignore any leading whitespace in the user’s greeting, and
    treat the user’s greeting case-insensitively.
    """
    user_input = input("Greeting: ").strip().lower()
    print(f"${value(user_input)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()