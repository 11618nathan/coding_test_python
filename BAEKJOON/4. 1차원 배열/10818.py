n = int(input())
l = [0 for i in range(n)]
l = list(map(int, input().split()))
l.sort()
print(l[0], l[-1])