
# 공간 복잡도
# 특정한 크기의 입력에 대해 알고리즘이 얼마나 많은 메모리를 차지하는지를 의미한다.

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
        