# Set
s1 = set([1,2,3])
print (s1) # {1, 2, 3}
s2 = set("Hello")
print (s2) # {'e', 'H', 'l', 'o'}

# Set 특징
# 1) 중복을 허용하지 않는다.
# 2) 순서가 없다(unordered)

# set자료형에 저장된 값을 인덱싱으로 접근 (리스트나 튜플로 변환)
s1 = set([1,2,3])
l1 = list(s1)
print (l1) # [1,2,3]
l1[0] # 1
t1 = tuple(s1)
print(t1) # (1,2,3)
t1[0] # 1

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 교집합, intersection
s1 & s2 # {4, 5, 6}
s1.intersection(s2) # {4, 5, 6}
# 합집합, union
s1 | s2 # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 차집합, difference
s1 - s2 # {1, 2, 3}
s2 - s1 # {8, 9, 7}
s1.difference(s2) # {1, 2, 3}
s2.difference(s1) # {8, 9, 7}

# 집합 자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print (s1) # {1, 2, 3, 4}
# 값 여러 개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1) # {1, 2, 3, 4, 5, 6}
# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print (s1) # {1, 3}