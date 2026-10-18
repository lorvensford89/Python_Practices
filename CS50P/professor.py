import random

def main():

    """
    In a file called professor.py, implement a program that:
        - Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3,
            the program should prompt again.
        - Randomly generates ten (10) math problems formatted as X + Y = , wherein each
            of X and Y is a non-negative integer with 𝑛 digits. No need to support operations
            other than addition (+).
        - Prompts the user to solve each of those problems. If an answer is not correct
            (or not even a number), the program should output EEE and prompt the user again,
            allowing the user up to three tries in total for that problem. If the user has
            still not answered correctly after three tries, the program should output the
            correct answer.
        - The program should ultimately output the user’s score: the number of correct answers out of 10.
    """


    level = get_level()                      # Checking level
    random_number1 = generate_integer(level) # Checking random generator
    random_number2 = generate_integer(level)

    numb_problems = 0
    max_numb_problems = 10

    attempts = 1
    max_attempts = 4

    error = "EEE"
    score = 0

    while numb_problems < max_numb_problems:
        n1 = random_number1
        n2 = random_number2
        sum = n1 + n2
        print(f"{n1} + {n2} = ", end="")
        try:
            user_input = int(input(""))
        except ValueError:
            print(error)
            attempts += 1
            if attempts == max_attempts:
                print(f"{n1} + {n2} = {sum}")
                random_number1 = generate_integer(level)
                random_number2 = generate_integer(level)
                attempts = 1
                numb_problems += 1
            continue

        if user_input != sum:

            print(error)
            attempts += 1
            if attempts == max_attempts:
                print(f"{n1} + {n2} = {sum}")
                random_number1 = generate_integer(level)
                random_number2 = generate_integer(level)
                attempts = 1
                numb_problems += 1
            continue

        elif user_input == sum:
            attempts = 1
            score += 1       

        random_number1 = generate_integer(level)
        random_number2 = generate_integer(level)

        numb_problems += 1

    print(f"Score: {score}")


def get_level():
    L = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level not in L:
                continue
        return level

def generate_integer(level):
    random_number = random.randint(0 if level == 1 else 10**(level - 1), 10**level - 1)
    return random_number


if __name__ == "__main__":
    main()