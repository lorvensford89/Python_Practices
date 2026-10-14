import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from el_library import lines
from el_library import bar

from pyfiglet import Figlet

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

    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font='slant')
    print(figlet.renderText("Lorvensford"))



    # TODO: Command-line Arguments


if __name__ == "__main__":
    main()