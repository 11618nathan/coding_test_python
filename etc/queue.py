
# 큐

from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.popleft()

print(queue)

# 역순으로 변경하기
queue.reverse
print(queue)
