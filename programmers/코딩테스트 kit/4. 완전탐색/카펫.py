#https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    count = brown + yellow
    for i in range(1, int(count**0.5)+1):
        if count % i == 0:
            j = count // i
            if (i-2) * (j-2) == yellow:
                return [j, i]
            
    return answer