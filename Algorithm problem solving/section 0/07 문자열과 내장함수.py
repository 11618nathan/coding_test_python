'''
문자열 내장함수
'''

s = 'Hello'
print(s.upper())
print(s.lower())
print(s)

r = s.upper()
print(r)
print(r.find("L"))
print(r.count("L"))
print(s[:2])
print(s[3:4])
print(len(s))
for i in range(len(s)):
    print(s[i], end=' ')
print()

for x in s:
    print(x, end=' ')
print()

for x in s:
    if x.isupper():
        print(x, end=' ')
print()

for x in s:
    if x.islower():
        print(x, end=' ')
print()

for x in s:
    if x.isalpha():
        print(x, end=' ')
print()

A = 'AZ'
for x in A:
    print(ord(x))
  
a = 'az'
for x in a:
    print(ord(x))

n = 65
print(chr(n))