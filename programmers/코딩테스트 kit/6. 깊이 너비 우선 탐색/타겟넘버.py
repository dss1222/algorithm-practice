def solution(numbers, target):
    answer = 0
    
    def dfs(index, current_sum):
        nonlocal answer
        
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return
        
        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])
        
    dfs(0, 0)
    return answer

from collections import deque

def solution2(numbers, target):
    queue = deque()
    queue.append((0, 0))
    count = 0
    
    while queue:
        index, current_sum = queue.popleft()
        
        if index == len(numbers):
            if current_sum == target:
                count += 1
        
        else:
            queue.append((index + 1, current_sum + numbers[index]))
            queue.append((index + 1, current_sum - numbers[index]))
            
    return count