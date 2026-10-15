import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))    # I need to understand this

from el_library import lines
from el_library import bar

import inflect


def main():
    pass


def problem_set4():
    """
    In a file called adieu.py, implement a program that prompts the 
    user for names, one per line, until the user inputs control-d. 
    Assume that the user will input at least one name. Then bid adieu 
    to those names, separating two names with one and, three names with 
    two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, 
    as in the below:

        Adieu, adieu, to Liesl
        Adieu, adieu, to Liesl and Friedrich
        Adieu, adieu, to Liesl, Friedrich, and Louisa
        Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
    """

    # Solution: 


if __name__ == "__main__":
    main()
