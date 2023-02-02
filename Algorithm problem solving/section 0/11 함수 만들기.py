'''
함수만들기
'''

def add(a, b):
    c = a + b
    print(c)

add(3, 2)
add(5, 7)

def add1(a, b):
    c = a + b
    return c
x = add1(3, 2)
print(x)

def add2(a, b):
    c=a+b
    d=a-b
    return c, d
print(add2(3, 2))

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

a = [12, 13, 7, 9, 10]

for y in a:
    if isPrime(y):
        print(y, end=' ')
    print()