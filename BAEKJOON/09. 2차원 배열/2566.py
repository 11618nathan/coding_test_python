import sys
input = sys.stdin.readline

result = 0
x, y = 0, 0

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] > result:
            result, x, y = arr[j], i, j

print(result)
print(x+1, y+1)