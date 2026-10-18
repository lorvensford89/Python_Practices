
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
    attempts = 0
    max_attempts = 3
    error = "EEE"

    random_number1 = generate_integer(level)                 # Problems to solve
    random_number2 = generate_integer(level)                 # TODO: handle the random numbers in the loop

    while numb_problems < max_numb_problems:
        
        print(f"{random_number1} + {random_number2} = ", end="")
        try:
            user_input = int(input(""))
            attempts += 1
        except ValueError:
            print(error)
            continue
        else:
            if user_input != (random_number1 + random_number1):
                print(error)
            if attempts == max_attempts:
                print(random_number1 + random_number2)

        numb_problems += 1



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
    random_number = random.randint(10**(level - 1), 10**level - 1)
    return random_number

    




if __name__ == "__main__":
    main()