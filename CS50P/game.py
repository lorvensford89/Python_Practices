import random

def main():
    problem_set()



def problem_set():
    """
    In a file called game.py, implement a program that:
        - Prompts the user for a level, 𝑛. If the user does not input a positive integer, 
            the program should prompt again.
        - Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
        - Prompts the user to guess that integer. If the guess is not a positive integer, 
            the program should prompt the user again.
                - If the guess is smaller than that integer, the program should output Too small! 
                    and prompt the user again.
                - If the guess is larger than that integer, the program should output Too large! 
                    and prompt the user again.
                - If the guess is the same as that integer, the program should output Just right! 
                    and exit.
    """



    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        
        guessed_number = random.randint(1, level)
        print(f"The guessed number: {guessed_number}")  # For checking

        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            else:
                print(guessed_number)
                if guess < guessed_number:
                    print("Too small!")
                    continue
                elif guess > guessed_number:
                    print("Too big!")
                    continue
                else:
                    print("Just right!")
                    break
                
        break

            
            

if __name__ == "__main__":
    main()