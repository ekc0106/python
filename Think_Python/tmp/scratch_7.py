## list

[10, 20, 30, 40] #리스트는 사각괄호~~
['crunchy frog', 'ram bladder', 'lark vomit']
['spam', 2.0, 5, [10, 20]]
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)

## mutable

print(cheeses[0])
numbers = [17, 123]
numbers[1] = 5
print(numbers)

'Edam' in cheeses
'Brie' in cheeses


## traversing  리스트의 원소를 한글자씩 읽어나가는거~

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

for x in []:
    print('This never happens.')

x = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
x[3]



## operation

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] * 4
[1, 2, 3] * 3


## slicing

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
t[:4]
t[3:]
t[:]

t[1:3] = ['x', 'y']
print(t)


## methods

t = ['a', 'b', 'c']
t.append('d') # 붙이는거~
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t2.insert(3, 'f') #사실 정확히하면,, 2,'f' 아닌가
print(t2)

t = ['a', 'b', 'c','b']
t.remove('b')
print(t) #아... 앞에있는거만 없애네

t.index('a') # 0 즉 맨앞에 있다~~

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
t.reverse()
t


## map, filter and reduce

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


t = [1, 2, 3]
sum(t)
add_all(t)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
capitalize_all(['aPPle','Bridge','caT'])
# 질문...
capitalize_all('aAf') #왜 이건 뭐...당연히 다 대문자로 나오지만,
capitalize_all(['aAf']) #원래 예시랑 이렇게 리스트로 넣으면 첫글자만 대문자가되고,..(이건그렇다쳐도) 나머지가 소문자가되는걸까
'aFa'.capitalize()

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
only_upper('aBdsE')

## deleting elements

t = ['a', 'b', 'c']
x = t.pop(1) # 해당 index의 원소를 빼오는 함수. ~.pop  그 후 t에서 또한 그 index인 원소가 빠져나감
print(t)
print(x)

t = ['a', 'b', 'c']
del t[1]
print(t)


t = ['a', 'b', 'c']
x = t.remove('b')
print(t)


t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)


## lists and strings

s = 'spam'
t = list(s)
print(t)
a=sorted(t)

#과제할 때 써먹어라~~
s = 'printing for the fjords'
t = s.split()
print(t)


s = 'spam-spam-spam'
delimiter = '-' #쪼갤 기호를 주면 그 기호에 맞게 쪼개줌~
s.split(delimiter)


t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)


## objects and values

a = 'banana'
b = 'banana'
a is b #같
# 은지 다른지~

a = [1, 2, 3]
b = [1, 2, 3]
a is b #흠...이건 무슨소린지 모르겟다..같은 123이지만 다른 저장공간에 저장한거라...?


## aliasing 별명관계...?위의 연장선

a = [1, 2, 3]
b = a
b is a

b[0] = 17
print(a) # 아 얘는 저장한게 아예 같은거라 b를 바꾸면 a도 바뀌는구나~


## list arguments

def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [4]
print(t3)

def bad_delete_head(t):
    t = t[1:] #잘못된 뻥션.. 함순데 함수자체의 인자를 건들이면 안됌..
bad_delete_head(letters) #출력 x

def tail(t):
    return t[1:]
tail(letters)

letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)



## examples

x = range(10)
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])

print(x[:3])
print(x[3:])
print(x[1:5])
print(x[-3:])
print(x[1:-1])

1 in [1,2,3]
0 in [1,2,3]

x = [1,2,3]
x.extend([4,5,6])
print(x)

x = [1,2,3]
y = x + [4,5,6]
print(x, y)

x.append(0)
print(x)



#과제설명
#10.3  write a function that takes a list of nmvers and returns the cummulative sum;
#       that is , a new list hwere the ith element is the sum of the  first i+1 elements frowm the original list
# 입력리스트 출력 누적합
    #[1,2,3]->[1,3,6]

range(len(x))
def cummulative_sum(x):
    csum = []
    for s in range(len(x)):
        csum.append(sum(x[:s+1]))
    return csum
x=[1,5,10]
cummulative_sum(x)
#10.7 Two words are anagrams if you can rearange the letters from one to spell the other.
#     write a function called 'is_anagram' that takes two strings and returns True if they are
#     anagrams
# 'anagram' 입력, 문자열 2개를 입력 값으로 받아서
	#True , False 를 리턴.
def is_anagram(a,b):
    x=list(a)
    y=list(b)
    z=sorted(x)
    w=sorted(y)
    print(z==w)
is_anagram('살자','자살')
is_anagram('이효리','이리효')
    #........(생략 아직 파일읽는거  안배웟으니 하지말아!~)
        # 10.10 word.txt란 파일 읽어서 리스트 생성(원소가 단어..)
	    #1번 .append 메소드
	    #2번 t=t+[x]
    	#두개의 시간비교... time 모듈써서 해라~~

#+++++++다음장에 또 설명있음





