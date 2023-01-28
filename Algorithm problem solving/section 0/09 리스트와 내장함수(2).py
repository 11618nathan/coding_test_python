'''
리스트와 내장함수(2)
'''
a = [16, 1, 12, 7, 32]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x)
print()

b = (1, 2, 3, 4, 5)
print(b[0])
# 튜플 값 변경 불가

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(30>x for x in a):
    print("YES")
else:
    print("No")
print()

if any(30>x for x in a):
    print("YES")
else:
    print("No")
print()