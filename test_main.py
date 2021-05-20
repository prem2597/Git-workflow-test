from main import *

def test_multiplication():
    assert multiplication(1,2,0) == 0
    assert multiplication(-1,2,3) == -6
    assert multiplication(10,-2,2) == -40
    assert multiplication(11,2,3) == 66
    assert multiplication(0,0,0) == 0
    assert multiplication(-1,-2,3) == 6
    assert multiplication(-1,-2,0) == 0
    assert multiplication(11,2,2) == 44
    print("All Test Cases Passed")


test_multiplication()
