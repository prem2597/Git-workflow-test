from main import *

def test_subtraction():
    assert subtraction(5, 5) == 0
    assert subtraction(-3, 3) == -6
    assert subtraction(-5, -5) == 0
    print("All test cases passed")

test_subtraction()
    