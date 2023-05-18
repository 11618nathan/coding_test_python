N = int(input())
# 본인 포함
cout = 1
s = 1
e = 1
sum = 1

while e != N:
    if sum == N:
        cout += 1
        e += 1
        sum += 1
    elif sum > N:
        sum -= s
        s += 1
    else:
        e += 1
        sum += e

print(cout)