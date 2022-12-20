'''
변수 입력과 연산자
'''

a = input("숫자 입력: ")
print(a)

a, b = input("숫자를 입력하세요: ").split()
print(a + b)
c = a + b
print(c)
print(type(c))

a, b = input("입력: ").split()
a = int(a)
b = int(b)
print(a + b)

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# 정수 + 실수 -> 실수
a = 1.6
b = 6
c = a + b
print(type(c))