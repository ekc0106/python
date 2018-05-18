1+1
a=3
if a>1
    print('a is greater than 1')
for a in [1,2,3]:
     print(a)

i=0
while i<3:
    i=i+1
    print(i)

for a in [1,2,3]:
    print(a)

# object.method 란걸 지원함. ex는 아래
(4+5j).real
(4+5j).imag
(4+5j).conjugate() #켤레복소수

#모듈 부르기.. import
import math
math.exp(-1.5)
math.cos(0)
from math import * #이렇게 쓰면 math 라는 모듈의 전체 function을 가져옴.. R에서 attach랑 비슷 이거하면 이제 'math.' 을 안해도됨.
#단 이렇게하면 불필요한 것도 가져오는 경우가 있어서....비효율적임.
cos(0)

not(7.5< 0.9 or 4==4)

message = "And now for something completely different"
n=17
# values and types
type('Hello, World!')
type(17)
type(3.2)
type('17')
type('3.2') 1,000,000
variables message = 'And now for something completely different'
n = 17 pi = 3.1415926535897932
type(message)
type(n)
type(pi)
# numbers
float(5)
int(5.2)
int(5.9)
complex(3.)
complex(0., 3.)
# operations
2.7 / 2 8 // 4
9 % 2
6 / 2 / 4
6 / (2 / 4)
# methods
(4+5j).real
(4+5j).imag
(4+5j).conjugate()
# mathematical functions
abs(-5.2)
abs(3+4j)
round(7.5)
import math
math.exp(-1.5)
math.cos(0)
from math import * cos(pi)
# comparison and logic
7 == 8
4 > 3.14
not (7.5 < 0.9 or 4 == 4)
# variable names and keywords
76trombones = 'big parade'
more@ = 1000000
class = 'Advanced Theoretical Zymurgy'
minute = 59
minute / 60
minute // 60
# interactive and script modes
miles = 26.2
miles * 1.61
print(miles * 1.61)
# sring operations
first = 'throat'
second = 'warbler'
print(first + second) print('Spam'*3)


## H.W.1 exercise2.3
#1번 반지름 'r'인 구의 부피가 4/3파이r^3 이다 r=5일때는? math.pi를써라..
#2번 cover price 가 $24.95다. 그리고 40% discount, shipping $3 first copy, 추가배송은 $0.75
#이랬을때 60copy를 주문한경우 sales cost는 얼마냐..
#3번 집에서 6시 52분에 출발한다. 1mile 달리는데 (8분15초 per mile), 3 mile은 (7분12초 per mile) 1mile은 8분15초per mile로 달림
#몇시도착할까?


#1번
from math import *
r=5
volume=4/3*pi*r**3
print(volume)
#2번
cover_price=24.95
copy=60
discount=0.6
cover_price*copy*discount + 3 + (copy-1)*0.75
#3번
total_seconds=(8*60+15)+(7*60+12)*3+(8*60+15)
totals=6*3600+52*60+total_seconds
hours=totals//3600
minutes=(totals-hours*3600)//60
seconds=(total_seconds)%60
print(hours,'시',minutes,'분',seconds,'초')

