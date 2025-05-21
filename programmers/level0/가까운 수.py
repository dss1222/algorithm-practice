#https://school.programmers.co.kr/learn/courses/30/lessons/120890
def solution(array, n):
    array.sort()

    answer = array[-1]
    min = 100
    
    for i in range(len(array) -1):
        if abs(array[i] - n) <= abs(array[i+1] - n):
            if abs(array[i] - n) < min:
                min = abs(array[i] - n)
                answer = array[i]

    return answer

print(solution([10, 11, 12, 14], 13))

def solution2(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer