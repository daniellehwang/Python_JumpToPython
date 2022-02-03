# List
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트 인덱싱
a = [1, 2, 3]
print (a)
a[0] #1
a[0] + a[2] #4
a[-1] #3

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
a[-1]
a[3]
a[-1][0] #a
a[-1][1] #b
a[-1][2] #c

# 삼중 리스트에서 인덱싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0] # life

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
a[0:2] # [1,2]
a = '12345'
a[0:2] # 12

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]

# 중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]

# 리스트 연산하기
a = [1, 2, 3]
# a[2] + "hi" error
str(a[2]) + "hi"
# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
a + b 

# 리스트 반복하기(*)
a = [1, 2, 3]
a * 3
# 리스트 길이구하기
a = [1, 2, 3]
len(a)

# 리스트 수정
a = [1, 2, 3]
a[2] = 4
print (a)

# del 함수 사용
a = [1, 2, 3]
del a[1]
print (a)

a = [1, 2, 3, 4, 5]
del a[2:]
print (a)

# 리스트 관련 함수
# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print (a)

a.append([5, 6])
print(a)

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)
# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print (a)
# 위치 반환(index)
a = [1, 2, 3]
a.index(3) #2
a.index(1) #0
# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)
# 리스트 요소 제거(remove), 리스트에서 첫 번째로 나오는 x를 삭제하는 함수
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
# 리스트 요소 끄집어내기(pop)
# pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다
a = [1, 2, 3]
a.pop()
print(a) #[1,2]

a.pop(1)
print(a) #[1,3]
# 리스트에 포함된 요소 x의 개수 세기(count)
# count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수
a = [1, 2, 3, 1]
a.count(1) #2
# 리스트 확장(extend)
# extend(x)에서 x에는 리스트만 올 수 있고 원래의 a 리스트에 x리스트를 더하게 된다
a = [1, 2, 3]
a.extend([4, 5]) # a += [4,5]와 같다
print(a)
b = [6, 7]
a.extend(b)
print(a)