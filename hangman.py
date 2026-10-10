"""
This is a hangman game.
"""

# There are modifications to be made.

import random

def main():
    lines(1)
    print("======================")
    print("     Hangman Game     ")
    print("======================")
    lines(1)
    hangman_logic()                 # TODO: 1) Read and validate the guess
    lines(2)                        #       2) Add it to the guessed letters
                                    #       3) If it's not in the word, increase attempts
                                    #       4) Rebuild the display from scratch, using all guessed letters
    #       5) Render it
    #       6) If no "_" remains, the player won. If attemps hit the max, the player lost. Otherwise, repeat. 


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

    print(f"Length of hangman list imaage: {len(hangman)}")
    print(f"Length of the guessed word: {len(computer_choice)}")

    max_attempts = len(computer_choice) + 3
    attempts = 0

    word_g = ""
    user_word_collection = []

    while True:
        word_g = ""
        if attempts == max_attempts:
            print("You have reached the maximum attempt!")
            break

        user_input = input("Enter a letter of the guessed word: ").strip().lower()
        if user_input.isdigit():
            print("Input should be a letter!")
            attempts += 1
            continue
        else:              
            for i in range(len(computer_choice)):   # not so sure yet about this
                if user_input in computer_choice:
                    word_g += computer_choice[i]
                    user_word_collection.append(user_input) # save the inputs of the user
                    #print(user_input)       # Needs to improve the logic of the game
                else:
                    word_g += " _ "
                   
                    #print(" _ ", end="")
                
    
    print(word_g)

def lines(a):
    for i in range(a):
        print("")
    


if __name__ == "__main__":
    main()

