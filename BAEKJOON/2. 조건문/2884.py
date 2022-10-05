h1, m1 = input().split()
h1 = int(h1)
m1 = int(m1)
m2 = m1 - 45
if (m2<0):
	h1 = h1 - 1
	if (h1 < 0 ):
		h1 = 24 + h1
	m2 = 60 + m2
print(h1, m2)