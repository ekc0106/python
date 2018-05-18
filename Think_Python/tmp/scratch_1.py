##3장


type(32) #str 는 문자 int는 정수 float은 실수

def print_lyrics():
    print("I'm a alumberjack, and I'm okay.")
    print("I sleep all night and I work ally day.")
type(print_lyrics)
print_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)
michael='Eric, the half a bee.'
print_twice(michael)

def cat_twice(part1, part2):
    cat=part1+part2
    print_twice(cat)
cat_twice(4,2)

# fruitful함수 : 결과값을 반환.
# void함수 : 실행은 되지만 결과값을 반환하지 않음.
x=math.cos(radians)
golden=(math.sqrt(5)+1)/2

result=print_twice('Bing')
print(result)
print(type(None))

#모듈을 가져오는 방법
import math
print(math)
print(math.pi)
print(pi) #하면 오류뜰거임..
from math import pi #이러면 바로 접근해도 에러안뜸.
print(pi)
#모든걸 다가져오려면 #단 불필요한것들도 다가져와버림.
form math import *
cos(pi)

def func1():
    print(x)
def func2():
    x +=1
x=4
func1()
func2() #이건 에러가뜸..
def func2():
    global x
    x+=1
x=4
func2()
x #이렇게 위에 global 해줘야 에러안뜸.. 함수속 x랑 지정해준 x랑 다른의미기에..

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
factorial(5)

#H.W. 과제