### chapter 14. ###

#import os
#os.chdir("c:/temp")
#os.getcwd()

## Reading and writing

fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)

fout.close()



## format operator
x = 52
fout.write(str(x)) #write의 인자는 문자열임..왜에러지?

camels = 42
'%d' % camels #문자열로 ㅍ변환하는 대신 포멧연산자 %를 사용
'I have spotted %d camels.' % camels

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

'%d %d %d' % (1,2) #d는 3갠데 갯수가 안맞아서...에러
'%d' % 'dollars' #정수형이 올자리에 문자열이 오니까 에러~ 타입이 안맞아서에러~



## filenames and paths

import os
cwd = os.getcwd() #os 모듈에서 getcwd라는 뻥션이 잇음.. Current Working Directory
print(cwd)

os.path.exists('output.txt') #이건 파일이 있는지 없는지, (폴더포함)
os.path.isdir('venv') #폴더(디렉토리)있는지 없는지.
os.listdir(cwd)  # 해당 디렉토리의 파일 및 폴더를 출력

#디렉토리 안의 모~든 파일을 보여줌(하위폴더의 파일까지도)
def walk(dirname: object) -> object:
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print (path)
        else:
            walk(path)
walk(cwd)
walk('C:\\Users\\kyucheol\\Desktop\\Juvis_project')


## catching exceptions

try:
    fin = fopen('output.txt')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong.')


## pickling 객체를 db에 적합한 문자열...로 변환,역변환한다..~?

import pickle
t = [1, 2, 3]
s = pickle.dumps(t)
print(s) #사람이 읽을수 있는 형태는 아니야~
t2 = pickle.loads(s)
print(t2)
t == t2
t is t2


## writing modules
# file_for_reading = open(’filename.txt’, ’r’) 이건 읽는거
# file_for_writing = open(’filename.txt’, ’w’) 이건 쓰는거
# file_for_appending = open(’filename.txt’, ’a’)
# file_for_writing.close() 이건 종료할때... 이거 꼭해줘야함.
# with open('filename.txt', 'r') as f:
#     data = function_that_gets_data_from(f) 머야 .. 교수님 문서파일에는 있는 코드인데 안되네

import re
starts_with_hash = 0
with open('output.txt', 'r') as f:
    for line in f:
        if re.match("^#", line): # check if a line starts with # ,,,#으로 시작된지 체크한다
            starts_with_hash += 1
starts_with_hash
def get_domain(email_address):
    """’@’ 기준으로 주소를 자르고 마지막 부분을 반환"""
    return email_address.lower().split("@")[-1]
get_domain('ekc0106@naver.com')
with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                    for line in f
                    if "@" in line) #뭐야 아까 위에부터 이거다 교수님 문서코드인데 다 안되넹..

## 구분자가 있는 파일
# 탭으로 분리된 파일
import csv
def process(date, symbol,price):
    print(date,symbol,price)
with open('~풀path', 'r', encoding='utf8',newline='') as f:
    reader = csv.reader(f, delimiter= '\t')
    # reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date,symbol,closing_price)

# wc.py
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

import wc

print(wc)
wc.linecount('wc.py')


## delimiated file

# tab delimited
import csv

def process(date, symbol, price):
    print(date, symbol, price)

#...아래는... 몰라
with open('C:/Users/kyucheol/PycharmProjects/고급플밍/tab_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    # reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

# colon delimited
with open('C:/Users/kyucheol/PycharmProjects/고급플밍/colon_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
    reader = csv.DictReader(f, delimiter=':')
    # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

# csv.writer
today_prices = { 'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }

with open('D:/Dropbox/�곗씠�� 諛깆뾽/Lecture/2018�� 1�숆린 怨좉툒�듦퀎�꾨줈洹몃옒諛�/肄붾뱶/comma_delimited_stock_prices.txt','w', encoding='utf8',newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])


## debugging

s = '1 2\t 3\n 4'
print(s)

print(repr(s))

# [과제 7] Exercise 14.1, 14.2, 14.6 (제출: 5월 10일)
# 14.1  The 'os' module provides a function called 'walk' that is similar to this one but more versatile.
#       Read the documentation and use it to print the names of the files in a given directory and its subdirectories.
# os 모듈에있는 walk 라는 펑션을 써서 해봐라
import os
def walk(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print (os.path.join(root, filename))
cwd = os.getcwd()
walk(cwd)
# 14.2 Write a function called 'sed' that takes as arguments a pattern string, a replacement string, and two filenames ;
#       it should read the first file and write the contents into the second file (creating it if neccessary). If the
#       pattern string appears anywhere in the file, it should be replaced with the replacement string.
#       If an error occurs while opening, reading, writing or closing files, your program should catch the exception,
#       print an error message, and exit. Solution : http://thinkpython.com/code/sed.py
#인자로 패턴(pattern) 문자열과 치환(replacement) 문자열과 두 개의 파일명을 인자로 받아들이는 함수
# sed를 작성하세요; 첫 번째 파일을 읽어서 콘텐트를 두 번째 파일에 (필요하면 만드세요) 써야 합니다.
# 만약 패턴 문자열이 파일에 등장하면, 치환 문자열로 바꿔야 합니다.

# 만약 파일을 열거나, 읽거나, 쓰거나, 닫을 때 오류가 발생한다면, 예외를 잡아서 오류 메시지를
# 인쇄한 후 종료해야 합니다. 답: http://thinkpython.com/code/sed.py.
# try:랑 except: 써서 에러처리를 해라
#  sed(pat,repl, file in, file out)..파일 있어야하겟죠..없으면 에러가 뜨겟죠? 그걸 에러를처리...?

def sed(pat, repl, file_in, file_out):
    try:
        fin = open(file_in, 'r')
        fout = open(file_out, 'w')
        for line in fin:
            line = line.replace(pat, repl)
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print ('Something went wrong')
sed('land','sea','output.txt','output2.txt')
#land 대신 sea로 바뀐후 그 파일이 output2.txt라는 파일로 저장되었다.
sed('haha','hoho','output4.txt','output3.txt')
#output4.txt라는 파일이 없기에 Something went wrong이라는 오류구문이 나옴

# 14.6 urllib 모듈은 URL을 다루고 웹에서 정보를 다운로드 하는 메쏘드들을 제공합니다. 다음 예는 thinkpython.com 에서 비밀 메시지를 다운로드하고 인쇄합니다:
#
# import urllib
#
# conn = urllib.urlopen('http://thinkpython.com/secret.html')
# for line in conn:
#     print line.strip()
# 이 코드를 실행하고 보이는 지시를 따르세요. 답:http://thinkpython.com/code/zip_code.py.
# 구글링을 해보셔야 할텐데..urllib...? 이게 3.버전에선 안될 수 있음.. 에러나면 알아서 찾아서 해라.
import urllib
def uszip():
    while True:
        zipcode = input('Zipcode >')
        if zipcode == 'done':
            print('end')
            break
        url = 'http://www.uszip.com/zip/' + zipcode
        comn = urllib.request.urlopen(url)
        for line in comn:
            line = line.strip()
            if b'<h2><strong>' in line:
                print(line)
            if b'Population' in line:
                print(line)
            if b'Longitude' in line:
                print(line)
            if b'Latitude' in line:
                print(line)
        comn.close()
uszip()
