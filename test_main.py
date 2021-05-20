from main import *

def test_armstrong():
    assert sum(10,20) == 30
    assert sum(-30,50) == 20
    assert sum(100.5,50.5) == 151

sum()

def test_subtraction():
    assert subtraction(5, 5) == 0
    assert subtraction(-3, 3) == -6
    assert subtraction(-5, -5) == 0
    print("All test cases passed")


    

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

test_multiplication()
test_quotient()
test_subtraction()
