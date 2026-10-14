import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from el_library import lines
from el_library import bar

from pyfiglet import Figlet
import random

def main():
    lines(2)
    bar("=")
    problem_set4()
    bar("=")
    lines(1)

def problem_set4():
    """
    Implement a program that:
        - Expects zero or two command-line arguments:
            1) Zero if the user would like to output text in a random font.
            2) Two if the user would like to output text in a specific font, 
                in which case the first of the two should be -f or --font and 
                the second of the two should be the name of the font.

        - Prompts the user for a str of text.
        - Outputs that text in the desired font.
    """

  

    # Command-line checking
    # Setting the package modules
    figlet = Figlet()
    font_list = set(figlet.getFonts())
    random_font = random.choice(figlet.getFonts())

    # Command-line checking
    if len(sys.argv) == 1:
        user_input = input("")
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
            user_input = input("")
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    print(figlet.renderText(user_input))

    



if __name__ == "__main__":
    main()