
# 숫자 카드 게임
# n행 n열로 구성
# 1. 각 행에서 최소값을 추출
# 2. 추출된 최솟값들에서 최대값 출력
 

# 행, 열 입력 받기
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    
    # min() 함수로 최소값 찾기
    min_value = min(data)

    # 각행의 최소값 중 최대값 찾기
    result = max(result, min_value)
    
# 결과 출력
print(result)
