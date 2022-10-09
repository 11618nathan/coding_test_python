
# 인접 행렬

graph = [[] for _ in range(3)]

# 0 노드 연결 저장
graph[0].append((1, 7))
graph[0].append((2, 5))

# 1 노드 연결 저장
graph[1].append((0, 7))

# 2 노드 연결 저장
graph[2].append((0, 5))

print(graph)
