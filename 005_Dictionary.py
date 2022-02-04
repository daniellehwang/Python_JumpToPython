# Dictionary
# {key1:value1, key2:value2, key3:value3}
# key에는 변하지 않는 값, value에는 변하는 값과 변하지 않는 값 모두 사용 가능
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a = {1: 'hi'}
a = { 'a': [1,2,3]}

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a) # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3]
print(a) # {1: 'a', 2: 'b', 'name': 'pey', 3: [1,2,3]}

# 딕셔너리 요소 삭제
del a[1] # del a[key]
print(a)

# 딕셔너리 사용 방법
{"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey':10, 'julliet': 99}
grade['pey']
grade['julliet']

a = {1:'a', 2:'b'}
print (a[1])
print (a[2])
print (a['a'])
print (a['b'])

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
dic['name']
dic['phone']
dic['birth']

# 딕셔너리 주의 사항
# Key는 고유한 값이므로 중복되는 Key 값을 성정하면 하나를 제외한 나머지는 모두 무시된다
a = {1:'a', 1:'b'}
print (a) # {1:'b'}

# key에 리스트는 쓸 수 없다, 하지만 튜플은 key로 쓸 수 있다
# 리스트는 값이 변할 수 있기 때문에 key로 쓸 수 없다. 변하지 않는 값이면 key로 쓸 수 있다
a = {[1,2]:'hi'} # error

# 딕셔너리 관련 함수
# Key 리스트 만들기(keys)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.keys() # dict_keys(['name','phone','birth'])

for k in a.keys():
    print(k)

# dict_keys 객체를 리스트로 변환    
list(a.keys())

# Value 리스트 만들기(values)
a.values() # dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기(items)
a.items()
# Key: Value 쌍 모두 지우기(clear)
a.clear()
print (a) # {}
# Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.get('name')
a.get('phone')
# None은 '거짓'
print(a.get('nokey')) # None
print(a['nokey']) # error
# 딕셔너리 안에 찾으려는 Key 값이 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때 
# get(x,'디폴트 값') 사용
a.get('foo', 'bar') # bar

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
'name' in a  # True
'email' in a # False