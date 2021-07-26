#if
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#if... else
money = True
if money:
 print("택시를")
print("타고")
 print("가라")

money = True
if money:
print(money)

x = 3
y = 2
x > y
print (x > y)
x < y
print (x < y)
x != y
print ( x != y)

#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.
money = 3000
if money >= 3000:
    print ("택시를 타고 가라")
else:
    print("걸어가라")

#and, or, not
money = 2000
card = True     #
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#x in s, x not in s
1 in [1, 2, 3]
1 not in [1, 2, 3]

#Tuple
'a' in ('a', 'b', 'c')
'j' not in 'python'

#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문에서 아무 일돈 하지 않게 설정하고 싶을때.
# 주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
