## string is a sequence

fruit = 'banana'
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)

letter = fruit[1.5]

len(fruit)

length = len(fruit)
last = fruit[length]
print(last)

print(fruit[-1])

fruit[0:5:2]    # step size 2
fruit[::-1]     # backward

# escape sequence

sentence = "He said, \"This parrot's dead.\""
sentence
print(sentence)
subjects = 'Physics\nChemistry\nBiology'
subjects
print(subjects)



## traversal

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# equivalently

for char in fruit:
    print(char)


prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)


## slicing

s = 'Monty Python'
print(s[0:5])
print(s[6:12])
fruit[:3]
fruit[3:]
fruit[3:3]


## print function

heading = '| Index of Dutch Tuplip Prices |'
line = '+' + '-'*16 + '-'*14 + '+'
print(line, heading, line,
      '|     Nov 23 1636 |        100 |',
      '|     Nov 25 1636 |        673 |', line, sep='\n')



## immutability

greeting = 'Hello, world!'
greeting[0] = 'J'

new_greeting = 'J' + greeting[1:]
print(new_greeting)


## searching

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
def find2(word, letter):
    index=0
    iter=0
    while iter < len(word):
        if word[iter] == letter:
            index= index +1
        iter = iter+1
    return index
find2('banana','n')
find('banana', 'n')

## counting

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


## string methods
word = 'banana'
new_word = word.upper() #object.upper 같이 .~~이런걸 method라고함. 함수같은거~
print(new_word)
word.find('na')
word.find('na', 3)

name = 'bob'
name.find('b', 1, 2) #시작점1, 끝점 2


a = 'java python c++ fortran'
a.isalpha() #알파벳이냐~?
b = a.title()
b
c = b.replace(' ', '!\n')
c
print(c)
c.index('Python') # \n은 한글자로 취급... 즉  Java!\nPython!\nC++!\nFortran 여기서 0,1,2,3,4,5,6번째에서 시작!



## in operator

'a' in 'banana'
'seed' in 'banana'

def in_both(word1, word2):
    for letter in word1: #word1에서 한글자씩 읽음.
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')



## string comparison
word = 'apple'

if word == 'banana':
    print('All right, bananas.')
else:
    print('babo')

if word < 'banana': #알파벳순으로 크다 작다를 따짐.
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')


## debugging

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)

    while j > 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

is_reverse('pots', 'stop') #length -1 로해서 하면 에러 안뜬다고하심..밑에처럼


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0: #원래 > 였는데>=로 고침.
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

is_reverse('pots', 'stop')

#과제 8장 1 4 11번

#8.1
def read_backward(word):
    index=1
    for char in word:
        a=len(word)-index
        index=index+1
        print(word[a])
read_backward('이효리')


#8.4
def find(word, letter, start):
    index = 0
    iter = start
    while iter < len(word):
        if word[iter] == letter:
            index = index + 1
        iter = iter + 1
    return index
find('Eom kyu cheol','o',0)
find('Eom kyu cheol', 'o',2)

#8.11
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return  True
        else:
            return  False
any_lowercase1('Aa')
any_lowercase1('aA')
# 함수는 return문을 만나는 순간 결과값을 돌려준 후 함수를 빠져나가게 된다.
# 그러므로 any_lowercase1함수는 첫번째 문자가 소문자인지 대문자인지만 보고 판단하므로 옳지 않게 작성된 함수이다.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
any_lowercase2('Aa')
#이 함수는 input이 무엇이든, 결과는 'c'라는 그냥 char자체가 소문자인지 묻고 맞다면 'True'를 출력하라 했기에,
#  항상 'True'값만 출력되는 함수다.

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
any_lowercase3('Aa')
any_lowercase3('aA')
#이 함수는 for문이 완료된 마지막글자가 소문자인지의 여부만 확인하는 함수이기에 옳지 않다.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
any_lowercase4('aA')
any_lowercase4('AA')
#이 함수는 or를 통해, 최소 한개라도 소문자를 포함하면 True 값을 갖기에 소문자가 한개라도 있으면 True를 출력하는 함수다.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return  False
    return True
any_lowercase5('aa')
any_lowercase5('Aa')
any_lowercase5('a a')
# 위의 함수는 input값에 소문자가 나오지 않는 순간, 바로 False값을 주며 모두 소문자일 경우 True를 반환한다.
# 약간 아쉬운 점이 있다면, 3번째 예시같이 띄어쓰기가 있는 소문자로만 이루어진 문자열은 공백때문에 False 값을 반환한다.
