
# 큰 수의 법칙
# 리스트 요소의 개수는 n
# 리스트에서 요소를 m번 더해서 가장 큰 수를 만든다
# 단, 더한 요소가 연속으로 k번 초과는 다른 수를 사용
# 요소의 값이 같을 경우 중복 사용 가능

# 위의 변수 n, m, k를 입력
n, m, k = map(int, input().split())

# n개의 리스트 요소의 값 입력
data = list(map(int, input().split()))

# 입력 받은 리스트 요소 정렬
data.sort()

# 가장 큰 수
# 오름차순 정렬과 리스트 인덱스는 0부터 시작이므로 입력한 n값 -1이 뒷값
first = data[n-1]

# 다음 큰 수
# first와 방식 동일
second = data[n-2]

# 결과값 저장
result = 0

# 핵심
# 최대값을 먼저 k먼 더한다. -> 먼저 실행
# k번 실행하여 결과값 저장 완료
# 다음 값을 1번 실행 후 다시 최대값 k번 반복

while True:
    # 최대 k번 실행
    for i in range(k):
        # 더하는 m번이 0일 경우
        if m == 0:
            # 탈출
            break
        # 결과에 최대값을 저장
        result += first
        m -= 1
    
    # 더하는 m번이 0일 경우
    if  m == 0:
        # 탈출
        break
    # 다음 최대값을 더함
    result += second
    m -= 1 

# 결과값 출력
print(result)
