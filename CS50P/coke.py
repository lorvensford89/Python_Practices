"""
In a file called coke.py, implement a program that prompts the user
to insert a coin, one at a time, each time informing the user of the
amount due. Once the user has inputted at least 50 cents, output how
many cents in change the user is owed. Assume that the user will only
input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
    accepted_coins = [5, 10, 25]
    savings_input = []


    while True:
        print("Amount Due:", 50)
        user_input = int(input("Insert Coin: "))

        if user_input in accepted_coins:
            savings_input.append(user_input)
            break


    while sum(savings_input) < 50:
        print("Amount Due:", 50 - sum(savings_input))
        user_input = int(input("Insert Coin: "))

        if user_input in accepted_coins:
            savings_input.append(user_input)

    print("Change Owed:", sum(savings_input) - 50)

main()




