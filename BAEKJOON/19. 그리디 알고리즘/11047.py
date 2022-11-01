n, k = map(int, input().split())

l = [0 for i in range(n)]

# 동전 개수 세기
cout = 0
# 값을 나눈 몫의 값을 저장할 변수
m = 0

for i in range(n):
    l[i] = int(input())

l.reverse()

for i in l:
    m = k // i
    k = k - (m * i)
    cout += m

print(cout)