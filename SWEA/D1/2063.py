n = int(input())
mid = (n // 2)

l = list(map(int, input().split()))

l.sort()
print(l[mid])