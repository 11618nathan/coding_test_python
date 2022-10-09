
# 시계 

# 지정한 시간까지 숫자 3이 포함된 모든 시간을 카운트

# 지정한 시간 입력
h = int(input())

count = 0

# 입력한 시간까지 실행
for i in range(h + 1):
    # 59분 동안 실행
    for j in range(60):
        # 59초 동안 실행
        for k in range(60):
            # 숫자 3이 포함된 시각을 카운트
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
