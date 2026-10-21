def main():
    problem_set()
    

def problem_set():
    """
    In a file called twttr.py, reimplement Setting up my twttr from 
    Problem Set 2, restructuring your code per the below, wherein 
    shorten expects a str as input and returns that same str but with
    all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase
    or lowercase.
    """

    # Solutions

    user_input = input("Input: ") 
    output = ("")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for vowel in user_input:
        if not vowel in vowels:
            output += vowel

    print("Output:", output)


if __name__ == "__main__":
    main()