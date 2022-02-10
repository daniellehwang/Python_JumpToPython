# Function
# 입력값을 가지고 어떤 일을 수행한 다음 그 결과물을 내는것
# 과일(입력) + 믹서(함수) = 주스(출력)
# 믹서는 과일을 입력받아 주스를 출력하는 함수

# 파이썬 함수 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
    
from unittest import result


def add(a, b):
    return a + b
# "이 함수의 이름(함수 이름)은 add이고 입력으로 2개의 값을 받으며 결괏값은 2개의 입력값을 더한 값이다."

a = 3
b = 4
c = add(a, b)
print(c) # 7

# 매개변수(parameter)와 인수(arguments) 
# 매개변수: 함수에 입력으로 전달된 값을 받는 변수
# 인수: 함수를 호출할 때 전달하는 입력값
def add(a, b): # a, b는 매개변수
    return a+b

print(add(3, 4)) # 3, 4는 인수

# 입력값 = 함수의 인수, 매개변수
# 결과값 = 출력값, 반환 값, 돌려주는 값

# 입력값과 결괏값에 따른 함수 형태
# 입력값 -> 함수 -> 결괏값

# 1) 일반적인 함수
# 입력값이 있고 결괏값이 있는 함수
# def 함수이름(매개변수):
#     <수행할 문장>
#     return 결과값

# def add(a, b):
#     result = a + b
#     return result

# 결괏값 받을 변수  = 함수이름(입력인수1, 입력인수2..)
a = add(3, 4)
print(a) # 7

# 2) 입력값이 없는 함수
# 결괏값 받을 변수 = 함수이름()
def say():
    return 'Hi'
a = say()
print(a)

# 3) 결괏값이 없는 함수
# 함수이름(입력인수1, 입력인수2, ..)
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3, 4) # 3, 4의 합은 7입니다.

a = add(3, 4) # 3, 4의 합은 7입니다.

a = add(3, 4)
print(a) # None

# 3) 입력값도 결괏값도 없는 함수
# 함수이름()
def say():
    print('Hi')
say() # Hi

# 4) 매개변수 지정하여 호출하기
def add(a, b):
    return a+b
result = add(a=3, b=7) # a에 3, b에 7을 전달
print(result) # 10
# 매개변수를 지정하면 순서에 상관없이 사용할 수 있다
result = add(b=5, a=3) # b에 5, a에 3을 전달
print(result) # 8

# 입력값이 몇 개가 될지 모를 때
# def 함수이름(*매개변수):
#     <수행할 문장>

# 여러 개의 입력값을 받는 함수 만들기
# args는 인수를 뜻하는 arguments
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result) # 6
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result) # 55

# 여러 개의 입력값을 의미하는 *args 매개변수 앞에 choice 매개변수가 추가 됨
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

# 매개변수 choice에 'add'가 입력된 경우 *args에 입력되는 모든 값을 더해서 15를 돌려주고
# 'mul'이 입력된 경우 *args에 입력되는 모든 값을 곱해서 120을 돌려줌
result = add_mul('add', 1,2,3,4,5)
print(result) # 15
result = add_mul('mul', 1,2,3,4,5)
print(result) # 120

# 키워드 파라미터 kwargs **
def print_kwargs(**kwargs):
    print(kwargs)

# kwargs는 keyword arguments    
print_kwargs(a=1)
{'a': 1}
print_kwargs(name='foo', age=3)
{'age': 3, 'name': 'foo'}

# 함수의 결괏값은 언제나 하나
# add_and_mul 함수는 2개의 입력 인수를 받아 더한 값과 곱한 값을 돌려주는 함수
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
result = (7, 12)
result1, result2 = add_and_mul(3, 4)

def add_and_mul(a, b):
    return a+b
    return a*b
result = add_and_mul(2, 3)
print(result) # 5

# return의 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)
say_nick('야호')
# 나의 별명은 야호입니다.
say_nick('바보')

# 매개변수에 초깃값 미리 설정하기
# say_myself 함수는 3개의 매개변수를 받아 마지막 인수인 man이 True면 "남자입니다." False면 "여자입니다."를 출력함
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself("박응용", 27)
say_myself("박응용", 27, True)
# 나의 이름은 박응용입니다.
# 나이는 27살입니다.
# 남자입니다.
say_myself("박응선", 27, False)
# 나의 이름은 박응용입니다.
# 나이는 27살입니다.
# 여자입니다.

def say_myself(name, man=True, old): # (name, old, man=True)
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
# error        

# 함수 안에서 선언한 변수의 효력 범위
# vartest.py
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

def vartest(hello):
    hello = hello + 1
    
# vartest_error.py
def vartest(a):
    a = a + 1
vartest(3)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1) return 사용하기
# vartest_return.py
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

# 2) global 명령어 사용
# vartest_global.py
a = 1
def vartest():
    global a
    a = a+1
    
vartest()
print(a)

# lambda
# lambda 매개변수1, 매개변수2, ...: 매개변수를 이용한 표현식
add = lambda a, b: a + b
result = add(3, 4)
print(result) # 7

# lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다
def add(a, b):
    return a+b

result = add(3, 4)
print(result) # 7