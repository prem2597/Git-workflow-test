import math
import numpy as np

def iscomposite(number):
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return True
    return False
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
    if not str(num1).isdigit() :
        return 'Arguments should be number type'
    if not str(num2).isdigit() :
        return 'Arguments should be number type'
    return num1 + num2


def tan_val(num) :
    if str(num).isdigit() :
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

# This method return True if the argument passed is not char

def isDigit(num) :
    if str(num).isdigit() :
        return True
    else :
        return False
def swap(x,y):
    temp = x
    x = y
    y = temp

def swapping(a,b):
    temp = a 
    a = b
    b = temp
    return a,b

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

