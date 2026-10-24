from fuel2 import convert, gauge


def test_catdog():
    assert convert("1/4") == 25
    assert gauge(25) == "25%"

def test_half():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"

def test_3_4():
    assert convert("3/4") == 75
    assert gauge(75) == "75%"

def test_full():
    assert convert("4/4") == 100
    assert gauge(100) == "F"

def test_empty():
    assert convert("0/1") == 0
    assert gauge(0) == "E"

