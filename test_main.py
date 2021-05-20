from main import isArmstrong

def test_armstrong():
    assert isArmstrong(153) == True
    assert isArmstrong(154) == False
    assert isArmstrong(22) == False

test_armstrong()