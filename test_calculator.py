import sys
from calculator import square

def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(5) == 25
    assert square(9) == 81
    try:
        assert square(10) == 101
    except AssertionError:
        sys.exit("Square of 10 wrong! Exiting...")

if __name__ == "__main__":
    main()