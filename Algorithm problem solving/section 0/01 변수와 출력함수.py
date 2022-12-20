'''
변수명 정하기
1. 영문, 숫자, _
2. 대소문자 구분
3. 문자, _ 로 시작
4. 특수문자x (&, % 등)
5. 키워드 사용x (if, for 등)
'''

# 대입 연산자
a = 1
A = 2
print(a, A)


# 한 번에 여러 개 선언
a, b, c = 1, 2, 3
print(a, b, c)


# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)


# 변수 타입
# int형
a = 123
print(type(a))
# 실수형 - 8바이트까지 출력
a = 12.1234567890123456789
print(a)
print(type(a))
# str형
a = 'laphayen'
print(type(a))


# 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
# sep
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='\n')
# end
print(a, end=' ')
print(b, c)