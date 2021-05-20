import math
import numpy as np

def power(x,y):
    if y == 0:
        return 1
    if y%2 == 0:
        return power(x,y // 2) * power(x,y // 2)
    return x*power(x,y // 2) * power(x,y // 2)
def order(x):
    n = 0
    while(x!=0):
        n=n+1
        x=x//10
    return n
def isArmstrong(x):
    n=order(x)
    temp=xsum1=0
    while(temp!=0):
        r=temp%10
        sum1=sum1+power(r,n)
        temp=temp // 10
    return (sum1 == x)

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

def mul_3num(a,b,c):
	return a*b*c
    
def get_abs(value):
    return abs(value)

def rem(a,b):
	return a%b

def quiotent(a, b):
    return a // b

def addition(a,b):
    return (a+b)

def expotential(base, exponent):
    return base ** exponent

def swap(x,y):
    temp = x
    x = y
    y = temp

def factorial(value):
    factorial = 1
    if value < 0:
        return("Sorry, factorial does not exist for negative numbers")
    elif value == 0:
        return("The factorial of 0 is 1")
    else:
        for i in range(1,value + 1):
            factorial = factorial*i
        return("The factorial of",value,"is",factorial)

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
    print(mul_3num(1,2,0))
    print(np.pi)
    print(subtraction(5,3))
    print(addition(10,20))
    print(expotential(3,5))
    print(get_abs(-100))

    print(swap(5,6))
    print(factorial(5))

    print(isArmstrong(153))


__init__()



