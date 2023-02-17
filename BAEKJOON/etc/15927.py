import sys,math
input = sys.stdin.readline
s = input().strip()
l = len(s)
if s == s[0] * l: print(-1)
elif s[:l//2][::-1] == s[math.ceil(l/2):]: print(l-1)
else: print(l)