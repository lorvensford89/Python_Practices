"""
This is a guessing word game in Python
"""

import random

def main():

    lines(2)
    print("=== Guessing Word Game ===")
    print("Total attempts: 5")
    print("==========================", end="")
    lines(2)

    game_logic()

    print("==========================", end="")
    lines(2)



def game_logic():
 
    words = [ "apple", "bridge", "candle", "dolphin", "engine",
            "forest", "guitar", "hammer", "island", "jungle", "kitten",
            "lantern", "mountain", "needle", "ocean", "pencil", "quartz",
            "rocket", "sunset", "turtle" ]

    for i in range(len(words)):
        print(i + 1, "-", words[i])
    lines(3)

    word_position = random.randint(0, 19)
    total_attempts = 5
    attempts = 0

    # for testing
    print(f"{word_position + 1}: {words[word_position]}")
    lines(2)

    while True:
        lines(2)
        user_choice = input("Enter the word: ")
        attempts += 1

        lines(2)

        if user_choice == words[word_position]:
            print("You have WON!")
            print(f"\"{words[word_position]}\" is correct")
    
            if attempts == 1:
                print("Damn! You guessed it in the first attempt.")
            elif attempts == total_attempts:
                print("My gosh! In the last attempt.")
            else:
                print(f"Attempts: {attempts}/{total_attempts}")

            break
        else:
            print(f"Incorrect!")
            print(f"Attempts: {attempts}/{total_attempts}")
            if attempts == total_attempts:
                print("Total attempts reached!")
                print(f"{attempts}/{total_attempts}")
                break

    lines(2)

        
def lines(a):
    for i in range(a):
        print("")

if __name__ == "__main__":
    main()
