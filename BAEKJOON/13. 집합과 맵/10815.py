N = int(input())
s_num = set(map(int, input().split()))
M = int(input())
m_num = list(map(int, input().split()))
for i in m_num:
    if i in s_num:
        print(1, end=' ')
    else:
        print(0, end=' ')