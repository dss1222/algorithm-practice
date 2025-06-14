def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
                
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
            
    return count

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])