n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (n + 1)
answer = -1

def dfs(v, target, cnt):
    global answer
    visited[v] = True
    
    if v == target:
        answer = cnt
        return
    
    for next in graph[v]:
        if not visited[next]:
            dfs(next, target, cnt + 1)
            
dfs(target1, target2, 0)
print(answer)