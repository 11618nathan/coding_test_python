T = int(input())
for i in range(T):
    num = list(map(int, input().split()))
    result = sorted(num)
    print(result[-3])