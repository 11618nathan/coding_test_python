n = int(input())

l = list(map(int, input().split()))

v = int(input())

cout = 0

for i in l:
    if  i == v:
        cout += 1

print(cout)