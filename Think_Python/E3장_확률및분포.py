###ChapterE3. 확률 및 분포 ###
from collections import Counter
import math, random


# conditional probability

def random_kid():
    return random.choice(["boy", "girl"]) #이건 리스트 안에있는걸 랜덤하게 골라내는 함수

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000): #반복문 쓸 때, 딱히 인덱스의 의미가 없을땐 저렇게 쓰기도함.
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print("P(both | older):", both_girls / older_girl)      # 0.514 ~ 1/2
print("P(both | either): ", both_girls / either_girl)   # 0.342 ~ 1/3


# uniform distribution

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    "returns the probability that a uniform random variable is less than x"
    if x < 0:   return 0    # uniform random is never less than 0
    elif x < 1: return x    # e.g. P(X < 0.4) = 0.4
    else:       return 1    # uniform random is always less than 1


# normal distribution

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1)   for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.show()

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend(loc=4) # bottom right
plt.show()

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0            # normal_cdf(-10) is (very close to) 0
    hi_z,  hi_p  =  10.0, 1            # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # consider the midpoint
        mid_p = normal_cdf(mid_z)      # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


# central limite theorem

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(p, n):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(p, n) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs,ys)
    plt.show()

make_hist(0.75, 100, 10000)

#[과제 9] <1> U(0,1)에서 난수를 1000개 발생하여 x축에는 표본수 n, y축에는 누적평균을 선그래프로 그리시오.
# 누적평균값은 n이 커짐에 따라 어떤 값을 수렴하는가?
import random, math
from matplotlib import pyplot as plt
def mean(x):
    return sum(x) / len(x)
data = [random.random() for _ in range(1000)]
xs = range(1001)
n_mean = [mean(data[0:(i+1)]) for i in range(xs)]
plt.plot(xs, n_mean,'-')
plt.show()
n_mean[-1]
# 0.5 로 수렴함을 알 수 있다.


# <2> random 모듈을 이용하여 숫자 맞추기 게임을 구현하시오.
#  컴퓨터가 랜덤하게 1과 100사이의 정수를 고르고, 사용자가 1과 100사이의 추측값을 주면 정답과 비교하여 적절한 메시지(가령 크다, 작다, 잘했어요 등)를 주시오.
# randint 쓰면 되겠지. 루프돌려서... 크다 작다는 이프문해서 그냥 하고.
from random import randint
sel_num = str(randint(1,100))
sel_num
while True:
    guess = input('>Guess')
    if guess > sel_num:
        print('크다')
    elif guess < sel_num:
        print('작다')
    else:
        print('잘했어요')
        break
