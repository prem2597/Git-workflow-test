import math

def tan_val(num) :
    if str(num).isdidgit :
        return math.tan(num)
    else :
        return 'Arguments should be number type'
def __init__():
    tan_value = tan_val(10)
    print('Tan value of number 10 is : ' + str(tan_val))
    
