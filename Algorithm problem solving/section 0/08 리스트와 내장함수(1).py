'''
리스트와 내장함수(1)
'''
import random as r

# 빈 리스트
a = []
print(a)
b = list()
print(b)

a = [1, 2, 3, 4, 5]
print(a[0])

b = list(range(1, 11))
print(b)

# 리스트 합치기
c = a + b
print(c)

a = [1, 2]
a.append(7)
print(a)
a.insert(0, 3)
print(a)
a.pop()
print(a)
     
# 인덱스 번호로 제거 가능
a.pop(1)
print(a)

a.remove(3)
print(a)

# 인덱스 번호 출력
print(a.index(2))

a=list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
# 인자값 중에 최소값 반환
print(min(7, 5))

r.shuffle(a)
print(a)
a.sort()
print(a)

# 내림차순으로 정렬
a.sort(reverse = True)
print(a)

a.clear()
print(a)s