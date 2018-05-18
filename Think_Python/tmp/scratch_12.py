## time

class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30
time.__dict__

## pure functions

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
done.__dict__ # ....분이 60분이 넘어가버림.

def print_time(t):
    print('%g:%g:%g' % (t.hour, t.minute, t.second))


print_time(done)


#pure function.. 기존의것을 건드리지 않음
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum
done = add_time(start, duration)
print_time(done)

## modifiers 기존의 것을..건드리는거
def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
#이거는...수정자는 편리하지만 오류 발생되기 쉬움. 되도록 사용 않는것이 좋음..
print_time(time)
increment(time,30)
print_time(time)

## prototyping and planning


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

#second 값을 minute으로, minute을 hour로.. ..
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
print_time(start)
print_time(duration)
done = add_time(start,duration)
print_time(done)
## debugging

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minutes >= 60 or time.second >= 60:
        return False
    return True

time= Time()
time.hour = -1
time.minute = 10
time.second=5
valid_time(time)

def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

add_time(time,start) #에러뜸

# assert 문을 이용할수도 잇음(조건을 만족하지 않을 때 예외 발생)
def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
add_time(time,start) #에러의 타입이 다르긴한데 코딩이 위보다 간결하니까..
#16.6 mul_time(일종의 퓨어뻥션)
#  아규먼트는 time, object, 숫자.. return value: time*숫자
# 그걸 이용해서 그.. 또다른 뻥션을 작성해라. 아규먼트는 time obj (finishing time in a race)
 # return : time object(average pace time per mile)
#Time 객체와 숫자를 받아서 Time 과 숫자의 곱을 포함하는 새 Time 객체를 돌려주는 함수 mul_time 를 작성하세요.
#그런 다음 경주에서 주행시간을 나타내는 Time 객체와 거리를 나타내는 숫자를 받아서 평균 패이스(마일당 시간)를 나타내는 Time 객체를 돌려주는 함수를 작성하는데 mul_time를 사용하세요.

def mul_time(time, dist):
    "time : 시간(s) , dist : 거리(mile)"
    time_per_mile =int(time_to_int(time)/dist)
    return (int_to_time(time_per_mile))
times = Time()
times.hour = 1
times.minute = 30
times.second = 30
times_per_mile = mul_time(times, 3)
print_time(times_per_mile) # 즉 3마일에 1시간 30분 30초가 걸린다면, 1마일에는 30분 10초가 걸린다.

##
 # 16.7 datetime.... date time..교재의 링크들가서 3.버전으로 들가라.
     # 1. current  date (2018년 4월23일) day of week (월요일) ..등등 매써드가 잇을거임.
import time
from datetime import datetime
today = datetime.today()
today.weekday()
def weekday_fun(weekday):
    if weekday == 0:
        print('월요일')
    elif weekday == 1:
        print('화요일')
    elif weekday == 2:
        print('수요일')
    elif weekday == 3:
        print('목요일')
    elif weekday == 4:
        print('금요일')
    elif weekday == 5:
        print('토요일')
    else:
        print('일요일')
weekday_fun(today.weekday())

     # 2. birthday ->input ... age # of days times  muinutes and second.. untile next birthday->output..
     # 즉 니 생일 날짜? 쓰고 그러면 아웃풋으로 다음 생일까지 몇일 몇시간 몇분 몇초 남았는지 계산하는 뻥션을 작성하라.
# datetime 모듈은 이 장에 나오는 Date 와 Time 객체와 유사한 date 와 time 객체를 제공하는데, 더 풍부한 메쏘드와 연산들을 제공합니다. http://docs.python.org/2/library/datetime.html에서 설명서를 읽으세요.

# datetime 모듈을 써서, 현재 날짜를 얻어서 요일을 인쇄하는 프로그램을 작성하세요.
# 입력으로 생일을 받아서 사용자의 나이와 다음 생일까지 남은 일, 시, 분, 초를 인쇄하는 프로그램을 작성하세요.
#(2)
import time
from datetime import datetime
today = datetime.today()
my_birthday = datetime(1995, 1, 6)
def time_to_birth(my_birth):
    age = today.year - my_birth.year
    my_birthday = my_birth.replace(year=today.year)
    if my_birth >= today:
        until_birth = my_birth - today
    else:
        my_birth = my_birth.replace(year = today.year +1)
        until_birth = my_birth - today
    print('나이 : ', age, '생일까지남은기간 : ',until_birth)
time_to_birth(my_birthday)
