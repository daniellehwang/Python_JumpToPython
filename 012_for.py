# for
# for 변수 in 리스트/튜플/문자열:
#     수행할 문장1
#     수행할 문장2

# 1) 전형적인 for 문
import re
from matplotlib.markers import MarkerStyle
from matplotlib.pyplot import contour


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# 2) 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
# (first, last) = (1, 2)

# 3) for문 응용    
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
marks = [90, 25, 67, 45, 80]
# marks1.py
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# 4) for문과 continue
# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)
    
# 4) for문과 함께 자주 사용하는 range 함수
# for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다. 
a = range(10)
a # range(0, 10)

a = range(1, 11)
a # range(1, 11)
# range 함수 예시
add = 0
for i in range(1, 11):
    add = add + i

print(add) # 55

#marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
# len함수는 리스트 안의 요소 개수를 돌려주는 함수다.
# len(marks) -> 5
# range(len(marks)) -> range(5)    
# number변수에 0~4까지 숫자 대입, marks[number] -> 90, 25, 67, 45, 80    

# for와 range를 이용한 구구단
for i in range(2, 10):      # 2~9
    for j in range(1, 10):  # 1~9
        print(i*j, end=" ")
    print('')
# 매개변수 end? 
# 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속 출력됨
# print(' ')?
# 2단, 3단을 구분하기 위해 두 번째 for문이 끝나면 결과값을 다음 줄부터 출력

# 리스트 내포(List comprehension) 사용
# a 리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담음
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result) # [3, 6, 9, 12]
# 리스트 내포
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]
# 짝수에만 3을 곱할때
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]
# 리스트 내포 문법
# [표현식 for 항목 in 반복가능객체 if 조건문]
# [표현식 for 항목1 in 반복가능객체1 if 조건문1
#         for 항목2 in 반복가능객체2 if 조건문2
#         for 항목n 반복가능객체n if 조건문n]