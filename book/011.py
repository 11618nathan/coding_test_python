#1874
N = int(input())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())

stack = []
num = 1
result = True
answer = ""
for i in range(N):
    s = nums[i]
    if s >= num:
        while s >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > s:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)