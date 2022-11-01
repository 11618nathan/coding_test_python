s = input().lower()

ss = list(set(s))

r = []

for i in ss:
    count = s.count(i)
    r.append(count)

if (r.count(max(r)) >= 2):
    print("?")
else:
    print(ss[r.index(max(r))].upper())