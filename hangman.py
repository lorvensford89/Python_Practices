"""
This is a hangman game.
"""

import random

def main():
    lines(1)
    print("======================")
    print("     Hangman Game     ")
    print("======================")
    lines(1)
    hangman_logic()
    lines(2)


def hangman_logic():

    # List of the word for the game
    words = [
    "python",
    "mountain",
    "bicycle",
    "thunder",
    "computer",
    "elephant",
    "galaxy",
    "pumpkin",
    "airport",
    "telescope"
    ]

    # Make the computer generate a random number
    computer_choice = random.choice(words)
    print(computer_choice)  # For directing the logic flow


    hangman = [
        """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
    ]



    while True:
      
        user_input = input("Enter a letter of the guessed word: ")
        if user_input.isdigit():
            print("Input should be a letter!")
            continue
        else:
            if user_input in computer_choice:
                print(user_input)       # Needs to improve the logic of the game
                break    

def lines(a):
    for i in range(a):
        print("")
    


if __name__ == "__main__":
    main()

