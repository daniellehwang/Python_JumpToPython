# If
from re import A
from numpy import _2Tuple


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# If 문의 기본 구조
# if 조건문:
#     수행할 문장1
#     수행할 문장2
# else:
#     수행할 문장A
#     수행할 문장B

# 들여쓰기 indentation
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3

# 비교 연산자
x = 3
y = 2
x > y # True
x < y # False
x == y # False
x != y # True

# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
# and, or, not 
# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# x in s, x not in s
1 in [1, 2, 3] # True
1 not in [1, 2, 3] # False
'a' in ('a', 'b', 'c') # True
'j' not in 'python' # True

# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문에서 아무 일도 하지 않게 설정
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
    
# elif
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."
# if & else
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
        
# elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

# if <조건문>:
#     <수행할 문장1>  
#     <수행할 문장2>
# elif <조건문>:  
#     <수행할 문장1>  
#     <수행할 문장2>
# elif <조건문>:  
#     <수행할 문장1>  
#     <수행할 문장2>
# else:  
#     <수행할 문장1>  
#     <수행할 문장2>

# if 문을 한 줄로 작성
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")   

# 조건부 표현식
score = 40
if score >= 60:
    message = "success"
else:
    message = "failure"
# 조건부 표현식 conditional expression
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
message = "success" if score >= 60 else "failure"