
# 좌표 이동 기초
# 상하좌우 간격 (1, 1)

# l: 좌1, r: 우1, u: 위1, d:아래1

# n은 이동 횟수 
n = int(input())

# 좌표
x, y = 1, 1

# 이동할 방향을 입력
plans = input().split()

# 상하좌우 움직일 방향 -> 2차원 배열로 x, y를 나누어 생각한다
# dx
# 0 0
# -1 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 , 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 방향
for plan in plans:
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
    
    # 좌표를 벋어날 경우 continue
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 좌표 이동
    x, y = nx, ny

print(x, y)
