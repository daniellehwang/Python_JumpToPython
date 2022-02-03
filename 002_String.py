# 문자열 만드는 방법
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short ,You need python'''

# 문자열에 작은따옴표 포함시키기
# Python's favorite food is perl
food = "Python's favorite food is perl"

# 문자열에 큰따옴표(") 포함시키기
# "Python is very easy." he says.
say = '"Python is very easy." he says.'

# 백슬래시를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# Life is too short
# You need python

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입
multiline = "Life is too short \nYou need python"

# 연속된 작은따옴표 3개''' 또는 큰따옴표 3개""" 사용
multiline='''
Life is too short
You need python
'''

multiline="""
Life is too short
You need python
"""
print(multiline)

# 문자열 연산
# 문자열 더해서 연결 Concatenation
head = "Python"
tail = " is fun!"
head + tail

# 문자열 곱하기
a = "python"
a * 2

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
len(a)

# 문자열 인덱싱과 슬라이싱
a = "Life is too short, You need Python"
a[3]
print(a[3])
a[0]
print(a[0])
a[12]
print(a[12])
a[-1]
print(a[-1])

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print (b)

a = "Life is too short, You need Python"
a[0:4]
a[0:3]
a[0:5]
a[5:7]
#시작 번호부터 문자열 끝까지
a[19:]
#시작부터 끝까지
a[:]
a[19:-7]

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[:8]
print(date, weather)

year = a[:4]
day = a[4:8]
weather = a[8:]
print(year, day, weather)

# 문자열 변경
# error
a = "Pithon"
a[1]
a[1] = 'y'

a = "Pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]

# 문자열 포매팅
# 숫자 바로 대입
"I eat %d apples." % 3
# 문자열 바로 대입
"I eat %s apples." % "five"
# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number
# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)

# %s 
"I have %s apples" % 3
"rate is %s" %3.234

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
"Error is %d%." % 98        # error
"Error is %d%%." % 98

# 포맷 코드와 숫자 함께 사용하기
# 정렬과 공백
"%10s" % "hi"
"%-10sjane." % 'hi'
# 소수점 표현하기
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234

# format 함수를 사용한 포매팅
# 숫자 바로 대입하기
"I eat {0} apples".format(3)
# 문자열 바로 대입하기
"I eat {0} apples". format("five")
# 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)
# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
# 왼쪽 정렬
"{0:<10}".format("hi")
# 오른쪽 정렬
"{0:>10}".format("hi")
# 가운데 정렬
"{0:^10}".format("hi")
# 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")
# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)
# { 또는 } 문자 표현하기
"{{ and }}".format()

# f 문자열 포매팅
name = 'hong'
age = 30
f'my name is {name}. I am {age} years old.'

age = 30
f'Next year I turn {age+1} years old.'
# 딕셔너리
d = {'name':'홍길동', 'age':30}
f'My name is {d["name"]}. I am {d["age"]} years old.'
# 정렬
f'{"hi":<10}' # 왼쪽 정렬
f'{"hi":>10}' # 오른쪽 정렬
f'{"hi":^10}' # 가운데 정렬
# 공백 채우기
f'{"hi":=^10}' # 가운데 정렬하고 '=' 문자로 공백 채우기
f'{"hi":!<10}' # 왼쪽 정렬하고 '!' 문자로 공백 채우기
# 소수점 표현
y = 3.42134234
f'{y:0.4f}'
f'{y:10.4f}'