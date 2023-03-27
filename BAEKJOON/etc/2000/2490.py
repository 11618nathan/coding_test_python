for i in range(3):
    n = map(int, input().split())
    r = sum(n)
    if r == 0:
        print("D")
    elif r == 1:
        print("C")
    elif r == 2:
        print("B")
    elif r == 3:
        print("A")
    elif r == 4:
        print("E")