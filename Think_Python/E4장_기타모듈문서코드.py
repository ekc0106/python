## E4. 기타모듈 ##
## random
import random

random.random() # random seed

random.seed(42)
random.random()
random.random()

random.seed(42)
random.random()
random.random()

random.uniform(-2, 2)

random.normalvariate(100, 15)

random.randint(5, 10) # 정수에 대해 랜덤난수..(5에서 10사이의 )

# random sequence

seq = [10, 5, 2, -3]
random.choice(seq)
random.shuffle(seq)
seq
random.sample(seq, 2)


## urllib

import urllib.request #웹스크래핑하는데 유용함.
# HTTP request
req = urllib.request.Request('http://www.wikipedia.org/w/api.php')
# catching exceptions
from urllib.error import URLError, HTTPError
try:
    response = urllib.request.urlopen(req)
except HTTPError as e:
    print('The server returned error code', e.code)
except URLError as e:
    print('Failed to reach server at {} for the following reason:\n{}'
          .format(url, e.reason))

# read the conent from the response
content = response.read()
# character set
charset = response.headers.get_content_charset()
# decode
html = content.decode(charset)



## datetimes

# date object
from datetime import date
birthday = date(2004, 11, 5)
notadate = date(2005, 2, 29) #2005년 2월 29일은 없음
today = date.today()
today

# time object
from datetime import time
lunchtime = time(hour=13, minute=30)
lunchtime
lunchtime.isoformat()

precise_time = time(4, 46, 36, 501982)
precise_time.isoformat()

witching_hour = time(24) #에러뜸

# datetime object
from datetime import datetime
now = datetime.now()
now
now.isoformat()
now.ctime()

# formatting
birthday.strftime('%A, %d %B %Y')
now.strftime('%I:%M:%S on %d/%m/%y')

lunch_time = datetime.strptime('09:32:00 July 16, 1969',
                               '%H:%M:%S %B %d, %Y')
print(lunch_time)
print(lunch_time.strftime('%I:%M %p on %A, %d %b %Y'))

#소문자b는 month에대해 3글자만, 대문자는 다~출력, 대문자 Y는 년도 다 출력, y는 뒤에 두개만.


