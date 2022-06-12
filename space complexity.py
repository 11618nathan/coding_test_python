
# 공간 복잡도 예제
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
        