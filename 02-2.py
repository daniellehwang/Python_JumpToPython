#using " "
food = "Python's faovrite food is perl"
print(food)

# #using ' '
# food = 'Python's favorite food is perl'
# print (food)

#including " in string
say = '"Python is very easy." he says.'
print(say)

#using \ including ' and "
food = 'Python\'s favorite food is perl'
print (food)
say = "\"Python is very easy.\" he says."
print (say)

#switching lines using \n
multiline = "Life is too short\nYou need Python"
print (multiline)

#using ''' or """ in row (better version)
multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)

#adding strings /concatenation
head = "Python"
tail = " is fun!"
head + tail
print (head + tail)

#multiply strings
a = "python"
a * 2
print (a * 2)

#multiply strings (advanced)
print ("=" * 50)
print ("My program")
print("=" * 50)

#counting strings
a = "Life is too short"
len(a)
print(len(a))

#string indexing
a = "Life is too short, You need Python"
a[3]
print (a[3])

b = "Life is too short, You need Python"
b[0]
print(b[0])
b[12]
print(b[12])
b[-1]
print(b[-1])
b[-0]
print(b[-0])
b[-2]
print(b[-2])
b[-5]
print(b[-5])

#string slicing
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

a = "Life is too short, You need Python"
a[0:4]
print(a[0:4])

a[0:3]
print(a[0:3])
# a[0:3] == 0 <= a < 3

a[0:5]
print(a[0:5])

a[0:2]
print(a[0:2])

a[12:17]
print(a[12:17])

a[19:]
print(a[19:])

a[:]
print(a[:])

a[19:-7]
print(a[19:-7])
# a[19] ~ a[-8] excludes a[-7]

#dividing string (slicing)
a = "20010331Rainy"
date = a[:8]
# excludes [8]
weather = a[8:]
print (date)
print (weather)

a="20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print (day)
print (weather)

#Changing string
# a="Pithon"
# print(a[1])
# a[1]='y'
# print(a[1])

a="Pithon"
a[:1]
print(a[:1])
a[2:]
print(a[2:])
a[:1] + 'y' + a[2:]
print(a[:1] + 'y' + a[2:])
# 'P'+'y' + 'thon'

# String Formatting
# 1. Integer
a = "I eat %d apples." % 3
print (a)
# 2. String
a = "I eat %s apples." % "five"
print(a)
# 3.
number = 3
a = "I eat %d apples." % number
print(a)
# 4. 2 or more
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days" % (number, day)
print(a)