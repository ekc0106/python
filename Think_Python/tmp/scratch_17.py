## descriptive statistics
from __future__ import division
from matplotlib import pyplot as plt
from collections import Counter
import math

num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16,
               15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12,
               12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
               10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
               8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
               4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
               2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)  # 204

largest_value = max(num_friends)  # 100
smallest_value = min(num_friends)  # 1

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]  # 1
second_smallest_value = sorted_values[1]  # 1
second_largest_value = sorted_values[-2]  # 49

print("num_points", len(num_friends))
print("largest value", max(num_friends))
print("smallest value", min(num_friends))
print("second_smallest_value", sorted_values[1])
print("second_largest_value", sorted_values[-2])


# center - mean


def mean(x):
    return sum(x) / len(x)


print("mean(num_friends)", mean(num_friends))


# center - median

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


print("median(num_friends)", median(num_friends))


# quantile

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


print("quantile(num_friends, 0.10)", quantile(num_friends, 0.10))
print("quantile(num_friends, 0.25)", quantile(num_friends, 0.25))
print("quantile(num_friends, 0.75)", quantile(num_friends, 0.75))
print("quantile(num_friends, 0.90)", quantile(num_friends, 0.90))


# center - mode

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]


print("mode(num_friends)", mode(num_friends))


# dispersion - range

def data_range(x):
    return max(x) - min(x)


print("data_range(num_friends)", data_range(num_friends))


# dispersion - variance
# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

def sum_of_squares(vec):
    return sum([elem ** 2 for elem in vec])


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


print("variance(num_friends)", variance(num_friends))


# dispersion - standard deviation

def standard_deviation(x):
    return math.sqrt(variance(x))


print("standard_deviation(num_friends)", standard_deviation(num_friends))


# dispersion - IQR

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


print("interquartile_range(num_friends)", interquartile_range(num_friends))

# covariance

daily_minutes = [1, 68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42,
                 31.22, 34.76, 54.01, 38.79, 47.59, 49.1, 27.66, 41.03,
                 36.73, 48.65, 28.12, 46.62, 35.57, 32.98, 35, 26.07, 23.77,
                 39.73, 40.57, 31.65, 31.21, 36.32, 20.45, 21.93, 26.02,
                 27.34, 23.49, 46.94, 30.5, 33.8, 24.23, 21.4, 27.94, 32.24,
                 40.57, 25.07, 19.42, 22.39, 18.42, 46.96, 23.72, 26.41,
                 26.97, 36.76, 40.32, 35.02, 29.47, 30.2, 31, 38.11, 38.18,
                 36.31, 21.03, 30.86, 36.07, 28.66, 29.08, 37.28, 15.28,
                 24.17, 22.31, 30.17, 25.53, 19.85, 35.37, 44.6, 17.23, 13.47,
                 26.33, 35.02, 32.09, 24.81, 19.33, 28.77, 24.26, 31.98,
                 25.73, 24.86, 16.28, 34.51, 15.23, 39.72, 40.8, 26.06, 35.76,
                 34.76, 16.13, 44.04, 18.03, 19.65, 32.62, 35.59, 39.43,
                 14.18, 35.24, 40.13, 41.82, 35.45, 36.07, 43.67, 24.61,
                 20.9, 21.9, 18.79, 27.61, 27.21, 26.61, 29.77, 20.59,
                 27.53, 13.82, 33.2, 25, 33.1, 36.65, 18.63, 14.87, 22.2,
                 36.81, 25.53, 24.62, 26.25, 18.21, 28.08, 19.42, 29.79,
                 32.8, 35.99, 28.32, 27.79, 35.88, 29.06, 36.28, 14.1, 36.63,
                 37.49, 26.9, 18.58, 38.48, 24.48, 18.95, 33.55, 14.24, 29.04,
                 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9, 27.2, 32.01, 29.27,
                 33, 13.74, 20.42, 27.32, 18.23, 35.35, 28.48, 9.08, 24.62,
                 20.12, 35.26, 19.92, 31.02, 16.49, 12.16, 30.7, 31.22, 34.65,
                 13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12, 24.42,
                 9.82, 23.39, 30.93, 15.03, 21.67, 31.09, 33.29, 22.61, 26.89,
                 23.48, 8.38, 27.81, 32.35, 23.84]

import numpy as np


def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n - 1)


print("covariance(num_friends, daily_minutes)", covariance(num_friends, daily_minutes))


# correlation

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0  # if no variation, correlation is zero


print("correlation(num_friends, daily_minutes)", correlation(num_friends, daily_minutes))

outlier = num_friends.index(100)  # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

print("correlation(num_friends_good, daily_minutes_good)", correlation(num_friends_good, daily_minutes_good))

#[과제 9] <1> U(0,1)에서 난수를 1000개 발생하여 x축에는 표본수 n, y축에는 누적평균을 선그래프로 그리시오.
# 누적평균값은 n이 커짐에 따라 어떤 값을 수렴하는가?
#
#
#
#
# <2> random 모듈을 이용하여 숫자 맞추기 게임을 구현하시오.
#  컴퓨터가 랜덤하게 1과 100사이의 정수를 고르고, 사용자가 1과 100사이의 추측값을 주면 정답과 비교하여 적절한 메시지(가령 크다, 작다, 잘했어요 등)를 주시오.
#
#
#


#  <3> Medals.csv, Athelete_Country_Map.csv, Athelete_Sports_MAP.csv 파일을 이용하여 대한민국의 연도별로 메달을 집계해 보시오.
#  또한 대한민국의 선수별로 총메달 갯수를 구하고 금메달, 은메달, 동메달 갯수 순으로 정렬하시오. (제출: 5월 24일)