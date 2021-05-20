from main import isArmstrong

def test_armstrong():
    assert isArmstrong(153) == True
    assert isArmstrong(153) == False

test_armstrong()