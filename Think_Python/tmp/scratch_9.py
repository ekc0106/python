### Chapter.12 ###
## tuples are immutable

t = 'a', 'b', 'c', 'd', 'e'
type(t)# or
t = ('a', 'b', 'c', 'd', 'e')

# tuple with a single element
t1 = 'a',
type(t1)
len(t1)

type(t2) #이러면 그냥 string...

t = tuple()
print(t) #빈튜플

t = tuple('lupins')
print(t)
print(t[0])
print(t[1:3])


mylist = [1,2]
mytuple = (1,2)
othertuple = 3, 4
mylist[1] = 3

try:
    mytuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


# immutable
t[0] = 'A'

# replacing is fine
t = ('A',) + t[1:]
print(t) #이런식으로 대체는 가능함.



## assignment

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname)
print(domain)


## as return values

t = divmod(7,3) #7을 3으로 나누면 몫은2 나머지는 1..튜플로 반환하는 모듈러연산
print(t)

quot, rem = divmod(7,3)
print(quot)
print(rem)

def min_max(t):
    return min(t), max(t)
min_max((3,1))
def sum_and_product(x, y):
    return (x+y), (x*y)

sp = sum_and_product(2,3)
print(sp)
s, p = sum_and_product(5,10)
print(s, p)



## variable-length arguments tuple

def printall(*args): #프로그램 실행시킬때... 어떤 아규먼트(인자값)를 주는거 옵션...? 그런걸 튜플로 받음.
    print(args)

printall(1, 2.0, '3')

t = (7, 3)
divmod(t) #두개의 아규먼트가 들어가야하는데.. 튜플이라는 하나짜리로 넌셈이 됨..그래서 에러가뜸.
divmod(*t)
divmod(t[0],t[1]) #이것도 되네~

## lists and tuples

t=[('a',0), ('b',1), ('c',2)]
for letter, number in t:
    print(number, letter)
#그냥혼자해본거..
tt=[['a,0'],['b',1],['c',2]]
for letter, number in tt:
    print(number, letter) #이건 안되넹..

for index, element in enumerate('abc'):
    print(index, element)


## dictionaries and tuples

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

dict_items([('a', 0), ('b', 1), ('c', 2)]) #왜있는거지...
d = dict(t)
print(d) #이렇게 튜플->딕셔너리로..바꿀 수 있음.

for key,val in d.items(): #우선 딕아이템으로바꾼후..~
    print(val, key)


directory = dict()
directory['Cleese','John'] = '08700 100 222'
directory['Chapman', 'Graham'] = '08700 100 222'
for last,first in directory:
    print(first, last, directory[last,first])


## Comparing tuples

(0,1,2) < (0,3,4) #첫번째(0과0)에선 비교불능이니... 두번째로 넘어감 (Q..그냥 False..아닌가?)
(0,1,2000000) < (0,3,4)

import random
a=random.random()

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

wdlist = ['dumb', 'apple', 'cliche']
sort_by_length(wdlist) #길이순서대로 sorting


## other examples 뭐지 이건 안한듯 수업.,,

t = (1, 'two', 3.)
t
t[1]
t[2] = 4

t = (1, ['a', 'b', 'c'], 0)
t[1][1] = 'c'
t #아하~ 튜플은 못바꾸지만, 안에있는 리스트는 바꿀수 있따~

a = [1, 2, 3]
b = ['a', 'b', 'c']

z = zip(a,b) # zip

for pair in z:
    print(pair)

list(zip(a,b))



##과제
# 12.1 Many of the buit_in functions use variable-length argument tuples. For example, max and min can take any number of
#  argument :
max(1,2,3) # execute
sum(1,2) # does not..
# write function called 'sumall' that takes any number of arguments and returns their sum.
def sumall(*args):
    return sum(args)
sum(1,2,3)
sumall(1,2,3)

# 12.2
# 길이가 같은 순서가 있다면 랜덤한 순서로...배치하라 라는...?
import random
def sort_by_length_random(words):
    t = []
    for word in words:
        t.append((len(word), random.random() ,word))

    t.sort(reverse=True)

    res = []
    for length, number , word in t:
        res.append(word)
    return res
wdlist = ['dumb', 'apple', 'clich']
sort_by_length_random(wdlist)
# 12.3  Write a function called 'most_frequent' that takes a string and prints the letters in decreasing order of frequency.
# Find text samples from several different languages and see how letter frequency varies between languages.
tuple('stops').# Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. Solution: http://thinkpython.com/code/most_frequent.py
a=tuple()
ex) stops 면 s가 2 t 1 o 1 p 1  이런식으로 많이나온순부터해서 프린팅 해라~ 다해볼필요없이 영어나 딴거...한개정도 간단히 시험삼아 해라.
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
def most_frequent(s):
    l=list()
    ll=list()
    for x in list(histogram(s).keys()):
        t=(histogram(s)[x],x)
        l.append(t)
    l.sort(reverse=True)
    return l
most_frequent('banana')
a=histogram('banana')
a.b