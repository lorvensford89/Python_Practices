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
    print(f"Your name is, {sys.argv[1]}.")


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
