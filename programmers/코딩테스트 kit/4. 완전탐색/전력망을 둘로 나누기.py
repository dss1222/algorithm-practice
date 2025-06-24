from collections import deque
from collections import defaultdict

def bfs(start, graph, visited):
    count = 1
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count
        
def dfs(start, graph, visited):
    count = 1
    visited[start] = True
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(neighbor, graph, visited)
    return count
        

def solution(n, wires):
    min_diff = n
    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i+1:]
        
        graph = defaultdict(list)
        for a, b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [False] * (n + 1)
        count = dfs(1, graph, visited)
        
        diff = abs(count - (n - count))
        min_diff = min(min_diff, diff)
    
    return min_diff