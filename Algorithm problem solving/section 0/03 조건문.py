'''
조건문 if(분기, 중첩)
'''

# == 비교 연산자
n = 7
if n == 7:
    # 들여쓰기 IndentationError
    print("lucky")

n = 5
if n != 7:
    # 들여쓰기 IndentationError
    print("lucky")

x = 15
if x>= 10:
    if x%2 == 1:
        print("10이상의 홀수")

x = 16
if x>= 10:
    if x%2 == 1:
        print("10이상의 홀수")

x = 7
if x>0 and x<10:
    print("10보다 작은 자연수")

x = 7
if 0<x<10:
    print("10보다 작은 자연수")

x = 10
if  x > 0:
    print("양수")
else:
    print("음수")


x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')