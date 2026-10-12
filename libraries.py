import random
import statistics
import sys

def main():
    lines(2)

    # random.randint(a, b)
    number = random.randint(1, 10)
    print(number)
    lines(1)

    # random.choice(seq) seq = list
    coin = random.choice(["tails", "head"])
    print(coin)
    lines(1)

    # random.shuffle(seq)
    players = ["Messi", "Cristiano", "Mbappe", "Lamine Yamal"]
    random.shuffle(players)
    for player in players:
        print(player, end=", ")

    lines(1)

    # statistics.mean(seq)
    a = 34
    b = 36
    mean_ = calc_mean(a, b)
    print(f"The average of {a} and {b} is {mean_}")

    lines(1)

    # sys.argv[a]   a: number of arguments
    """
    try:
        print(f"Your name is, {sys.argv[1]}.")
    except IndexError:          # Preventing the program to crash by handling exceptions
        print("The use of command-line arguments: ")       
        print("- Too few arguments!")
        lines(2)
        name = input("You were supposed to enter your name; but do it here: ")
        print(f"Your name is {name}.")
    else:
        print("You actually wrote something in the command-line after executing the program")
    finally:
        lines(1)
        print("You have used the 'sys' module.")
    """

    # handling using conditions
    if len(sys.argv) < 2:
        #print("Too few arguments!")
        sys.exit("Too few arguments!")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments!")
        # print("Too many arguments!")
    
    print(f"Your name is {sys.argv[1]}")





def lines(a):
    for i in range(a):
        print("")

def calc_mean(a, b):
    
    numbers = []
    numbers.append(a)
    numbers.append(b)  # this is just for practing
    m = statistics.mean(numbers)

    return m

if __name__ == "__main__":
    main()
