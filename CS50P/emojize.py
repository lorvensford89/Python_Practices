import emoji

def main():
    lines(2)
    problem_set4()
    lines(1)


def problem_set4():
    """
    implement a program that prompts the user for a str in English and 
    then outputs the “emojized” version of that str, converting any codes
    (or aliases) therein to their corresponding emoji.
    """

    table = []
    text = ""

    user_input = input("Input: ")
    print("Output: ", end="")

    table = user_input.split(", ")
    if len(table) == 2:
        text = table[0] + " " + table[1]
    else:
        text = user_input

    print(emoji.emojize(text, language="alias"))

    



def lines(a):
    for i in range(a):
        print()



if __name__ == "__main__":
    main()