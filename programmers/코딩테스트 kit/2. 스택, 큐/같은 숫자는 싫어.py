def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))