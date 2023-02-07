arr = [5, 3, 7, 9, 2, 5, 2, 6]
# 파이썬 가장 큰 값 초기화
arrMin=float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin=arr[i]
print(arrMin)

for x in arr:
    if x<arrMin:
        arrMin=x
print(arrMin)