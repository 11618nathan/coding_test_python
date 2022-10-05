h1, m1 = input().split()
h1 = int(h1)
m1 = int(m1)
c1 = input()
c1 = int(c1)
m2 = m1 + c1

if (m2>59):
	h1 = h1 + (int(m2/60))
	if (h1>23):
		h1 = h1 % 24
	m2 = m2 % 60

print(h1, m2)
