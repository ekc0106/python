eng2sp =dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])

print(eng2sp['four']) #없으니까 안나와~

len(eng2sp)

'one' in eng2sp
'uno' in eng2sp #이렇듯.. in 함수를 쓸때는 키값을 가지고 잇느냐 없느냐 해야함

vals = eng2sp.values()
'uno' in vals #이런식으로 해야 값들을 찾을 수 있음.


## a set of counters

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)


## looping 사전에서 루프를 사용하여 키들을 훑을 수 있음.

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)


## reverse lookup

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError('value does not appear in the dictionary')

h = histogram('parrot')
print(h)
k = reverse_lookup(h, 2)
print(k)
k = reverse_lookup(h, 3)


## dictionaries and lists

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse) #여기선 1, 2기 키로 바뀌고 string값이 값으로 들어감~~

t = [1, 2, 3]
d = dict()
d[t] = 'oops' #리스트같이 변하기 쉬운거는 키가 될 수 없다.!


## memos

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

fibonacci(3)
fibonacci(5)
## global variables 전역변수..의 예로는 flag를 들 수 있음. 다음은 출력의 디테일을 조정하는 vervose라는 플래그임

verbose = True

def example1():
    if verbose:
        print('Running example 1')

example1()

been_called = False

def example2():  # wrong
    been_called = True

example2()
print(been_called)
#밖의 변수를 함수 안에서 맘대로 못바꿈.
def example2():  # correct
    global been_called
    been_called = True
#위와 달리 굳이 밖에있는 변수를 함수안에서 바꾸려면 global 함수를 쓰면 바꿀 순 있음.

example2()
print(been_called)

count = 0

def example3():
    global count
    count += 1

example3()
print(count)

known = {0:0, 1:1}

def example4():
    known[2] = 1

example4()
print(known)

def example5():
    global known
    known = dict()

example5()
print(known)

#과제.
# 11.2 dictionaries have a method called 'get' that takes a key and a default value. If the
# key appears in the dictionary, 'get' returns the corresponding  value; otherwise it returns
# the default value. For example:
h= histogram('apdfa')
print(h)
h.get('a',0)
h.get('b',0)
#뭐지 이제부터 해라
def histogram(s):
    d = dict()
    for c in s:
        dic_value=d.get(c,0)
        dic_value += 1
        d[c]=dic_value
    return d
histogram('parrot')
# 11.3 keys 메쏘드를 이용해서 알파벳순서대로 키값을 프린트해주면됨
def print_hist(h):
    alpha=sorted(h)
    for c in alpha:
        print(c, h[c])
h = histogram('parrot')
h.keys()
print_hist(h)
# 11.4 키값이 있으면 value값을 주면 모든값을 전체를 리스트형태로 출력하고 없으면 엠티리스트를 주느
# 식으로 해라~.
c=[0]*7
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError('value does not appear in the dictionary')
h = histogram('parrot')
print(h)
k = reverse_lookup(h, 2)
print(k)
k = reverse_lookup(h,1)
a.app
len(a)
def reverse_lookup(d, v):
    a=[]
    for k in d:
        if d[k] == v:
            a.append(k)
    return a
k=reverse_lookup(h,1)
print(k)
k=reverse_lookup(h,2)
print(k)
k=reverse_lookup(h,3)
print(k)
