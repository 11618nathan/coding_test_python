# 1부터 n까지 홀수
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        print(i, end=' ')
print()

# 1부터 n까지 합
for i in range(1, n+1):
    sum = sum + i
print(sum)

# n의 약수
for i in range(1, n+1):
    if n % i == 0:
       print(i, end=' ')