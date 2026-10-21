

def main():
    """
    In a file called twttr.py, reimplement Setting up my twttr from Problem 
    Set 2, restructuring your code per the below, wherein shorten expects a 
    str as input and returns that same str but with all vowels (A, E, I, O, and U)
    omitted, whether inputted in uppercase or lowercase.
    """
    
    user_input = input("Input: ")
    print(shorten(user_input))
    
    
def shorten(word):
    output = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for vowel in word:
        if not vowel in vowels:
            output += vowel

    return output
    

if __name__ == "__main__":
    main()