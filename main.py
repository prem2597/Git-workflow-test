
def subtraction(a,b):
    return a-b


import math
import numpy as np


def multiplication(a, b, c):
    return a*b*c

def add(num1, num2) :
    if not str(num1).isdidgit() :
        return 'Arguments should be number type'
    if not str(num2).isdidgit() :
        return 'Arguments should be number type'
    return num1 + num2


def tan_val(num) :
    if str(num).isdidgit :
        return math.tan(num)
    else :
        return 'Arguments should be number type'

def mul_num(a,b):
    multiply=a*b
    return multiply
    

def rem(a,b):
	return a%b

def quiotent(a, b):
    return a // b

def addition(a,b):
    return (a+b)

def __init__():
    a, b = 10, 5
    q = quiotent(a, b)
    print(q)
    print(multiplication(a, b, q))
    tan_value = tan_val(10)
    print('Tan value of number 10 is : ' + str(tan_val))
    addition_result = add(3,5)
    print('Addition of numbers 3 and 5 is : ' + str(addition_result))
    print(rem(10,3))
    print(mul_num(5,10))
    print(np.pi)
    print(subtraction(5,3))
    print(addition(10,20))
    
__init__()

