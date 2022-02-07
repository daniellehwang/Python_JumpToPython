# Bool
# True or False
a = True
b = False

type(a) # <class 'bool'>
type(b) # <class 'bool'>
1 == 1  # True
2 > 1
2 < 1

# 자료형의 참과 거짓
a = [1, 2, 3, 4]
while a:
    print(a.pop()) # 4 3 2 1
    
# while 문
# 조건문이 참인 동안 조건문 안에 있는 문장을 반복해서 수행한다.
# while 조건문:
#     수행할 문장

if []:
    print("참")
else:
    print("거짓")
# 거짓
if [1,2,3]:
    print("참")
else:
    print("거짓")
# 참

# 불 연산
bool('python') # True
bool('') # False, ''문자열은 빈 문자열이므로 bool 연산의 결과로 불 자료형인 False를 돌려준다.
bool([1,2,3]) # True
bool([]) # False
bool(0) # False
bool(3) # True
