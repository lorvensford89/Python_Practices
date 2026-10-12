import random

def main():
    # .randint(a, b)
    number = random.randint(1, 10)
    print(number)
    lines(1)

    # .choice(seq) seq = list
    coin = random.choice(["tails", "head"])
    print(coin)
    lines(1)

    # .shuffle(seq)
    players = ["Messi", "Cristiano", "Mbappe", "Lamine Yamal"]
    random.shuffle(players)
    for player in players:
        print(player, end=", ")

    lines(1)


def lines(a):
    for i in range(a):
        print("")

if __name__ == "__main__":
    main()
