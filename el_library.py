# Personal library

from pyfiglet import Figlet     # I like that package

def lines(a):
    for i in range(a):
        print()

def bar(symbol):
    print(symbol * 30)

def my_name(name):
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font='slant')
    print(figlet.renderText(name))