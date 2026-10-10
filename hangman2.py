import random
from words_list import words

hangman_art = {
                0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}



def display_man(wrong_guesses):
    lines(2)
    print("=============")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("=============", end="")
    lines(2)

def display_hint(hint):
    lines(2)
    print(" ".join(hint))
    lines(2)

def display_answer(answer):
    lines(2)
    print("".join(answer))
    lines(1)

def lines(a):
    for i in range(a):
        print("")


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True


    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed_letters:
            print(f"|{guess}| is already guessed.")
            continue

        # keeping track of the letters that already guessed
        guessed_letters.add(guess)  

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            lines(2)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            lines(2)
            is_running = False
        
if __name__ == "__main__":
    main()