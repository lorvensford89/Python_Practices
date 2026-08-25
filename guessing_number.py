"""
This is a practice of GUESSING NUMBER GAME designed in Python
"""

# TODO: 1) Check the unnecessay keyword "continue"
#       2) Polish

import random

def main():
    guessing_number()


def lines(a):
    for i in range(a):
        print("\n", end="")

def guessing_number():
    print("======================")
    print(" GUESSING NUMBER GAME")
    print("======================")
    lines(1)
    print("The guessed number is between (1 - 20)")
    lines(2)

    # Generate random numbers from 1 to 20
    # 5 attempts maximum
    number = random.randint(1, 20)
    attempt = 0
    max_attempt = 5

    while True:
        print(number)   # for checking
        if attempt == max_attempt - 1:
            print("Last attempt ->")

        lines(1)
        n = input("Enter the guessing number: ")
        if n.isdigit():
            n = int(n)
            if n < 1 or n > 20:
                print("Number should be (1 - 20)")
                continue

            attempt += 1

            lines(1)
            if attempt == max_attempt and n != number:
                print("YOU LOST! You have reached the maximum attempts.")
                print("Thank you for playing")
                break

            if n > number:
                print("Too high!")
                print(f"Attempts: {attempt}/{max_attempt}")
                continue
            elif n < number:
                print("Too low!")
                print(f"Attempts: {attempt}/{max_attempt}")
                continue
            else:
                print(f"CONGRATULATIONS, YOU WON! {n} is the correct number.")
                if attempt == 1:
                    print("DAMN, you got it in the first attempt. That's some work. Well done!")
                elif attempt == max_attempt:
                    print("You got it in the last attempt. Great job!")
                else:
                    print(f"Attempts: {attempt}/{max_attempt}")
            lines(2)
            break
        else:
            print("Enter numbers (1 - 20)")
            attempt += 1
            lines(2)
            continue

main()