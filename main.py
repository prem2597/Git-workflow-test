
import math

def tan_val(num) :
    if str(num).isdidgit :
        return math.tan(num)
    else :
        return 'Arguments should be number type'

def mul_num(a,b):
    multiply=a*b
    return multiply

def mul_3num(a,b,c):
	return a*b*c
    

def rem(a,b):
	return a%b

def quiotent(a, b):
    return a // b

def __init__():
    a, b = 10, 5
    q = quiotent(a, b)
    print(q)
    tan_value = tan_val(10)
    print('Tan value of number 10 is : ' + str(tan_val))
    print(rem(10,3))
    print(mul_num(5,10))
    print(mul_3num(1,2,0))


__init__()
