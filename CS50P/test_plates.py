from plates2 import is_valid

def test_first():
    assert is_valid("HELLO") == "Valid"

def test_second():
    assert is_valid("HELLO, WORLD") == "Invalid"

def test_third():
    assert is_valid("GOODBYE") == "Invalid"

def test_fourth():
    assert is_valid("CS50") == "Valid"

def test_fifth():
    assert is_valid("CS05") == "Invalid"

def test_sixth():
    assert is_valid("50") == "Invalid"