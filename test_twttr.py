from twttr2 import shorten

def test_twitter():
    assert shorten("twitter") == "twttr"

def test_name():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_cs50():
    assert shorten("CS50") == "CS50"
