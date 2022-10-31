n = 10
count = 0
l1 = [0 for i in range(10)]
l2 = [0 for i in range(10)]

for i in range(10):
    l1[i] = int(input())
for i in range(10):
    l2[i] = l1[i] % 42

r = list(set(l2))
print(len(r))