def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
                
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer

from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for i in range(n):
                if computers[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
            
    return answer
