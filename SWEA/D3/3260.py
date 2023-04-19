T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print('#%d %d' %((tc+1), A+B))