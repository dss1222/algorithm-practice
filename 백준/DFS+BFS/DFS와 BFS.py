from collections import deque

# 1. 입력 받기
n, m, start = map(int, input().split())  # 정점 수, 간선 수, 시작 노드
graph = [[] for _ in range(n + 1)]  # 인덱스를 정점 번호와 맞추기 위해 n+1

# 2. 간선 정보 저장 (양방향)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 3. 정점 번호 작은 것부터 방문하기 위해 정렬
for i in range(1, n + 1):
    graph[i].sort()

# 4. DFS (재귀)
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node, visited)

# 5. BFS (큐)
def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

# 6. 실행
visited_dfs = [False] * (n + 1)
dfs(start, visited_dfs)
print()
bfs(start)
