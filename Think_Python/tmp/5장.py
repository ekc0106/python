## modulus operator

quotient = 7/3
print(quotient)

remainder = 7 %3
print(remainder)


## Boolean expressions

5 == 5
5 != 6

type(True)
type(False)


## logical operators

17 and True #숫자의 경우 0만 False, 그외에는 True로 보긴함..


## conditional executtion
x = 1

if x > 0:
    print('x is positive')

if x < 0:
    pass        # does nothing

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

y = 3

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


## recursion
#일종의 재귀함수.
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Hello', 2)


## keyboard input

text = input()
print(text)

name = input('What is your name?\n')

print(name)

prompt = 'What is the velocity?\n'
speed = input(prompt)
int(speed)
type(sqrt(4**2))
#과제2 (앞에파일 이어서)
def check_fermat(a,b,c,n):
    if (a<=0) or (b<=0) or (c<=0) or (n <= 2):
        print("you input a wrong value")
    else:
        if c**n == (a**n) + (b**n):
            print('Holy smokes, Fermat was wrong!')
        else:
            print("No, that doesn't work.")
check_fermat(3,4,5,3)
type(1)==int
def check_fermat():
    a = int(input('input a which is a positive integer'))
    b = int(input('input b which is a positive integer'))
    c = int(input('input c which is a positive integer'))
    n = int(input('input n which is greater than 2'))
    if (a<=0) or (b<=0) or (c<=0) or (n <= 2):
        print("you input a wrong value")
    else:
        if c ** n == (a ** n) + (b ** n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")
check_fermat()
1