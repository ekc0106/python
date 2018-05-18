## user-defined types

class Point(object):
    """Represents a point in 2-D space."""

print(Point)
blank = Point()
print(blank)
blank.__dict__ # 이런거구만.

## attributes
blank.x = 3.0
blank.y = 4.0
print(blank.x)
print(blank.y)
print('(%g, %g)' % (blank.x, blank.y))
print(blank.x, blank.y) #아 위에는 저렇게 멋있게 되고 이건 이리 밋밋하게 프린트 되는구나~
import math
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)

def print_point(p): #포인트타입을 받아서...값을 찍어냄
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)


## rectangles 이거는 위쓰 헤이트 코너..세가지를 가짐

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """
box.__dict__
box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0


## instances as return values

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
box.__dict__
center = find_center(box)
print_point(center)


## objects are mutable

def grow_rectangle(rect, dwidth, dheight): #아규먼트는 렉탱글,폭에대한증분,높이에대한 증분.. 이경우는 코너 변함x니까 ... 그냥 높이랑 폭의증분만..(?)
    rect.width += dwidth
    rect.height += dheight

print(box.width)
print(box.height)
print_point(box.corner)
grow_rectangle(box, 50, 100) #폭은 50, 높이는 100만큼 증가시켜라
print(box.width)
print(box.height)
print_point(box.corner)


## copying

p1 = Point()
p1.x = 3
p1.y = 4

import copy
p2 = copy.copy(p1)

print_point(p1)
print_point(p2)
p1 is p2
p1 == p2

box2 = copy.copy(box)
box.__dict__
box2.__dict__
box2 is box
box2.corner is box.corner #얘는 트루나옴...그래서 밑에처럼 디카피 시켜줘야함 그럼 둘다 뽈스나올꺼임

box3 = copy.deepcopy(box)
box3.__dict__
print_point(box3.corner)
box3 is box
box3.corner is box.corner


## debugging

p = Point()
p.x = 0
p.y = 0
print(p.z) #z라는 어트리뷰트가 존재하지않는다라는 에러가뜸

type(p)
#아래는 특정 어트리뷰트가 있는지 없는지를 알려주는 뻥션
hasattr(p, 'x')
hasattr(p, 'z')


#과제
# 15.1 distance -between-point 를 써라 input값으로 두개의 아규먼트(인자,,여기선 point타입임)를 가짐.->그들간의 아웃풋을 줘야함.
 이경우에는 주의할점이 아규먼트로써 포인트타입 두개를 넘겨받아서 그걸가지고서 매쓰펑션에서 유클리드 거리구하면됨.
#(x1,y1) , (x2,y2) 거리할 때 루트만.매쓰펑션에서 가져오면되는거임.~

def distance_between_points(p1, p2):
    import math
    return( math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))
p1 = Point()
p2 = Point()
p1.x = 0
p1.y = 0
p2.x = 3
p2.y = 4
distance_between_points(p1,p2)
#15.2 move_rectangle 이라는 뻥션을 작성해라. 렉탱글을 받고, dx,dy를 받아서(얼마만큼 움직일거냐..) width나 height는 변함x,
# 하지만 코너의 좌표만 dx, dy 만큼 움직이면 됨.
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    return (rect)
rect = Rectangle()
rect.width = 100
rect.height = 200
rect.corner = Point()
rect.corner.x = 0
rect.corner.y = 0
rect.__dict__
print_point(rect.corner) # 현재 rect은 corner가 (0,0) 이고 너비가 100, 높이가 200인 rectangle이다.

move_rectangle(rect, 1, 2)
rect.__dict__
print_point(rect.corner) # move_rectangle 함수를 쓴 후의 rect은 corner가 (1,2) 이며, 너비가 100, 높이가 200인 rectangle이다.

# 15.3 위의 move rectangle 을 변형해서 만들어봐라.->새로운 rectangle 을 생성..위에서처럼 코너값만 옮기는식이 아니라
#  return 새로운 rectangle....
box.__dict__
print_point(box.corner)
def modified_move_rectangle(rect, dx, dy):
    import copy
    rect1 = copy.deepcopy(rect)
    rect1.corner.x += dx
    rect1.corner.y += dy
    return (rect1)
box1 = modified_move_rectangle(box, 1, 2)
box1.__dict__
print_point(box1.corner)
box.__dict__
print_point(box.corner)
# 위와 같이 새로운 box1이 생성되어 코너를 1,2를 옮겨도 box는 변함이 없음을 알 수 있다.
# 참고로 2번의 move_rectangle을 쓰면,
box1 = move_rectangle(box, 1, 2)
box.__dict__
print_point(box.corner)
# 보시다시피 코너가 (0, 0)인 box를 x축으로 1만큼 y축으로 2만큼 옮긴 rectangle을 box1으로 지정했지만,
# 기존의 box의 코너도 (1, 2)로 되었음을 알 수 있다.