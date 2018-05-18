## updating variable

x = x + 1

x = 0
x = x + 1
x

## while statement

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')
countdown(4)

def sequence(n):
    while n != 1:
        print(n),
        if n % 2 == 0:
            n = n // 2  #(몫, 정수나누기..)
        else:
            n = n * 3 + 1
sequence(6)

# break

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')

# square root
epsilon = 1e-5
a = 2
x = 1

while True:
    print(x)
    y = (x + a / x) / 2
    if (abs(y - x) < epsilon):
        break
    x = y
math.sqrt(2)

eval('1+2+3')

# H.W.
# 7.1 5장의 print_n(재귀)을 while문으로.:
def print_n(s,n):
    if n<=0:
        return
    while n>0:
        print(s)
        n=n-1
print_n(3,5)
# 7.4 eval('1+2+3')하면 str(문자열)을 받아들여서 계산해주는거임.
# eval_loop를 만들어봐라...사용자 문자열 입력->계산->출력  ....=>while문을써서 done이라는 문자열이나올떄까지 반복
def eval_loop(x):
    if type(x) != str:
        print('The input is not a string.')
    else:
        while True:
            input1 = input('>')
            if input1 == 'done':
                print(eval(x))
                break
eval_loop(1+1)
eval_loop('1+1')
a=()