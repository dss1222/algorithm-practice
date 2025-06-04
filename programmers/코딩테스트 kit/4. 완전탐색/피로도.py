def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0
    
    def dfs(current_k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n):
            min_needed, consume = dungeons[i]
            if not visited[i] and current_k >= min_needed:
                visited[i] = True
                dfs(current_k - consume, count+1)
                visited[i] = False
                
    dfs(k, 0)
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
