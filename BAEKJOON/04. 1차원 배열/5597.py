num = [i for i in range(1, 31)]

for i in range(28):
    r = int(input())
    num.remove(r)

print(min(num))
print(max(num))