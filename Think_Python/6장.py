## return values

# area of a circle
import math
def area(radius):
    temp = math.pi * radius ** 2
    return temp

def area(radius):
    return math.pi * radius ** 2

# multiple return

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

# wrong x가 0일때는 값이 안나옴.
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x


print(absolute_value(0))


## incremental development

# example
# step 1
def distance(x1, y1, x2, y2):
    return 0.0


# test
distance(1, 2, 4, 6)


# step 2
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0


# test
distance(1, 2, 4, 6)


# step 3
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    print('dsquared is', dsquared)
    return 0.0


# test
distance(1, 2, 4, 6)

# step 4
import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result

# test
distance(1, 2, 4, 6)


## composition
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
circle_area(0,0,2,5)

# more concisely
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


## boolean functions

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


is_divisible(6, 4)

is_divisible(6, 3)



# more cosisely
def is_divisible(x, y):
    return x % y == 0


# unconditional statement
if is_divisible(x, y):
    print('x is divisible by y')

# equivelently
if is_divisible(x, y) == True:
    print('x is divisible by y')


## more reccusions

def factorial(n):
    if n == 0:
        return 1  #종료조건
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result
factorial(3)
# checking types
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial('fred')
factorial(-2)


## debugging
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result


factorial(4)



#피보나치수열 fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(7)

#과제3
#그냥 간단하네..
#Exercise 6.1. Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.
def compare_function(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
compare_function(5,1)
compare_function(5,5)
compare_function(0,1)
#Exercise 6.8. The greatest common divisor (GCD) of a and b is the largest number that divides
#both of them with no remainder
#최대 공약수... 테스트 하는것도 삽입해라 적당한 인풋으로.
만약 a>b면, a%b=r이라하자..
gcd(a,b)=gcd(b,r)...
gcd(a,b)=gcd(max(b,a%b),min(~~~~))
gcd(a,0)='a'
뭐 이런식으로...function 짜봐라.
13%5

def gcd(a,b):
    r=max(a,b)%min(a,b)
    if r==0:
        return min(a,b)
    else:
        a=min(a,b)
        b=min(a,b,r)
        return gcd(a,b)
gcd(8445,10)
gcd(36,1652)
