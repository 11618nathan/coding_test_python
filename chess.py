
# 체스

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 말이 움직이는 모든 경우
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 결과 출력하는 변수
result = 0

# 움직일 수 있는 경우 출력
for step in steps:
    # 가로 이동
    next_row = row + step[0]
    # 세로 이동
    next_column = column + step[1]

    # 이동 시 칸을 넘어가지 않는 경우만 계산
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        # 해당되면 결과값 저장
        result += 1

# 결과 출력
print(result)
