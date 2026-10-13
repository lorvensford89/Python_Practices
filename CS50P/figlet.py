import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import el_library
from pyfiglet import Figlet

def main():
    el_library.lines(2)
    el_library.bar()
    problem_set4()
    el_library.bar()
    el_library.lines(1)


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

    # Examples from the Figlet module
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font='slant')

    name = "EL"
    print(figlet.renderText(name))

    # TODO: Command-line Arguments


if __name__ == "__main__":
    main()