#### 17장 ####

## printing objects

class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 00
Time.print_time(start) #이렇게 잘안쓰고 아래처럼
start.print_time() #이렇게 많이씀


## init method

class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)) #.2d% 두자리 정수

    def __init__(self, hour=0, minute=0, second=0):  # init 이건 함수의 초기값(디폴트값) 을 지정해주는거
        self.hour = hour
        self.minute = minute
        self.second = second


time = Time()
time.print_time() #입력안해도 스스로 디폴트값으로 나오게됨

time = Time(9)
time.print_time()

time = Time(9, 45)
time.print_time()


## str method

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


time = Time(9, 45)
print(time)


## operator overloading

def int_to_time(seconds): #인티저 투 타임 이건 초를 넣으면 알아서 시 분 초로 출력해주는 함수 만든거임~
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):          #time_to_int 타임투 인티져... 타임을 받아서 인티져로 내놓는거
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __add__(self, other):      # 타임에 대해서 덧셈을 할 수 있게끔 한거임~
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)


start = Time(9, 45)
duration = Time(1, 35)
type(start)
type(duration)
print(start + duration) # 시간에 대해 덧셈이 되었네~


## type based dispatch

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __add__(self, other):
        if isinstance(other, Time): #어떤 크래스의 인스턴스인지 체크해주는거?
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds): #이거 추가햇네 아규먼트가 셀프고, 인크레먼트는 앞에있는 걸 다 세컨드로 만들고 더한후 다시 시간으로만드는거
        seconds += self.time_to_int()
        return int_to_time(seconds)


start = Time(9, 45)
duration = Time(1, 35)
print(start + duration) #이렇게 시간+시간일땐 아까 위처럼 알아서 잘 더하고
print(start + 1337) #이렇게 시간+정수 꼴로 나와도 뒤의 정수를 '초'로 받고 알아서 잘 시간 더할 수 있도록.. 근데 왜 안되지.?
#이거 아래함수 실행시키고 하면 되는데....위에껄로만은 안되네  ##ㅇ다시하니까 또 되네..뭐지
print(1337 + start) #이거는 에러.. 앞에는 시간이 나와야 하도록 함수 짰었음


class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other): #이걸 통해 아래의 print(1337 +start) 도 순서 뒤바뀌게 알아서 잘 읽어서 함수 실행되도록 하는거임
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


start = Time(9, 45)
print(1337 + start)


## polymorphism

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d


t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
histogram(t)

def __radd__(self, other): #이건 문서에 중간껴있길래 그냥 추가했음...뭐 아더가 0인것도 받는다고 했는데..뭔지모르겠ㅇ므
    if other ==0:
        return self
    else:
        return self.__add__(other)


t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)


## debugging
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.__dict__)  #hasattr 이외에 .__dict__ 속성을 이용하여 객체 속성에 접근 #이게 과제 2번라네
Point().__dict__ #이러면 알아서 디폴트값으로

def print_attributes(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))


print_attributes(p)


###과제


#17.3 Point 클래스 str 메소드를 작성...
#Point 클래스의 str 메쏘드를 작성하세요. Point 객체를 만들고 인쇄하세요.
class Point(object):
    def __init__(self,x = 0 , y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
point = Point(20,18)
print(point)

#17.4 Point 클래스의 add 메쏘드를 작성하세요. add를 하는데 sum까지 되는지.. 확인을 해보세요,
def make_point(x,y):
    point=Point(x,y)
    return point

class Point(object):
    def __init__(self,x = 0 , y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        return self.add_point(other)

    def add_point(self, other):
        sum_point = Point(self.x + other.x ,self.y + other.y)
        return sum_point

point1 = Point(1,2)
point2 = Point(3,4)
print(point1+point2)
def sumall(*args):
    return sum(args)
sum(point1, point2)
total = sumall([point1, point2])
print(total)

##sum까지 해보랫는데 나는 sum 이안되네... 나중에 다시해보자


#17.5 add->point+object,,,  new point!!  튜플 이면 알아서 쪼개서 어쩌구저쩌구 되도록
        #ㄴ>tuple,,,,,,,,
class Point(object):
    def __init__(self,x = 0 , y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        return self.add_point(other)
    #
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.increment(other)
    def add_point(self, other):
        sum_point = Point(self.x + other.x ,self.y + other.y)
        return sum_point
    def increment(self, other):
        other= Point(other[0] + self.x, other[1] + self.y)
        return other

p1 = Point(1,2)
p2 = Point(3,4)
p3 = (3,4)
print(p1 + p2) # 두번째 연산자가 Point 여도 결과를 반환하며.
print(p1 + p3) # 두번째 피연산자가 튜플이여도 결과를 반환함
