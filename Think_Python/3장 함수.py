### Chapter.3 ###
# function calls

type(32)


# type conversion functions

int('32')
int('Hello')

int(3.99999)
int(-2.3)

float(32)
float('3.14159')

str(32)
str(3.14159)


# math functions

import math
print(math)

signal_power = 5
noise_power = 1
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)

math.sqrt(2.0)/2.0


# composition

x = math.sin(degrees / 360.0 * 2 * math.pi)

x = math.exp(math.log(x+1))

hours = 2
minutes = hours * 60    # correct

hours * 60 = minutes    # left side : variable


# new functions

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print(print_lyrics)
type(print_lyrics)

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()


# parameters and arguments

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')
print_twice('Spam '*4)

import math
print_twice(math.pi)
print_twice(math.cos(math.pi))

michael = 'Eric, the half a bee.'
print_twice(michael)


# variables and parameters are local

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

print(cat)


# fruitful/void functions

radians = math.pi / 2
x = math.cos(radians)   # assign
golden = (math.sqrt(5)+1)/2

math.sqrt(5) # In script mode, the return value is not displayed.


result = print_twice('Bing') # displays but not return
print(result)
print(type(None)) # None type


# importing with from

import math
print(math)
print(math.pi)

print(pi)
from math import pi
print(pi)

from math import *
cos(pi)


## scope

def func1():
    print(x)

def func2():
    x += 1

x = 4
func1()
func2()

def func2():
    global x
    x += 1

x = 4
func2()
x


## recursive function

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

factorial(5)

#과제2. p.29 ex3.4번 (1)~(4) + 5.3번 그건 다음파일에 스겟삼
#1번.
def do_twice(f):
    f()
    f()
def print_spam():
    print ('spam')
do_twice (print_spam)
#2번.
def do_twice(f,x):
    f(x)
    f(x)
#3번.
def print_twice(y):
    print (y)
    print (y)
#4번.
do_twice(print_twice,'spam')
#5번.
def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)

do_four(print_twice,1)

