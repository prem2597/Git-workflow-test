from main import *

def test_quotient():
    assert multiplication(0,1) == 0
    assert multiplication(-1,1) == -1
    assert multiplication(10,-2) == -5
    assert multiplication(10,5) == 2
    assert multiplication(0,0) == "not possible"
    assert multiplication(10,3) == 3.33
    assert multiplication(20,5) == 4
    assert multiplication(11,2) == 5.5
    print("All Test Cases Passed")


test_quotient()