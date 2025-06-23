n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
answer = -1

def dfs(v, target, cnt):
    global answer    
    visited[v] = True

    if v == target:
        answer = cnt
        return answer
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, target, cnt+1)
            
dfs(target1, target2, 0)
print(answer)