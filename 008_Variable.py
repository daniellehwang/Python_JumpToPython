# Variable 변수
a = 1
b = "python"
c = [1,2,3]
# 변수이름 = 변수에 저장할 값
# 변수는 객체를 가리키는 것. 객체는 자료형이다.
a = [1, 2, 3]
id(a) # 4303029896 a변수가 가리키는 메모리 주소

# 리스트 복사
a = [1,2,3]
b = a
id(a) # 4303029896
id(b) # 4303029896
a is b # True

a[1] = 4
a # [1, 4, 3]
b # [1, 4, 3]

# 1. [:] 이용
a = [1, 2, 3]
b = a[:]
a[1] = 4
a # [1, 4, 3]
b # [1, 2, 3]
# 2. copy 모듈 이동
from copy import copy
a = [1, 2, 3]
b = copy(a)
b is a # False

a = [1, 2, 3]
b = a.copy() 

# 변수를 만드는 여러 가지 방법
# 튜플
a, b = ('python', 'life')
# 튜플
(a, b) = 'python', 'life'
# 리스트 
[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
a # 5
b # 3