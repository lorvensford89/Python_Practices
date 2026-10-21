from bank import value

def test_Hello():
    assert value("Hello") == 0

def test_grettingname():
    assert value("Hello, Newman") == 0

def test_Hey():
    assert value("Hey") == 20

def test_Howyoudoing():
    assert value("How you doing?") == 20

def test_Whatshappening():
    assert value("What's happening?") == 100

def test_Whatsup():
    assert value("What's up?") == 100