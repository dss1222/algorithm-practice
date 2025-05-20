#https://school.programmers.co.kr/learn/courses/30/lessons/120852
def solution(n):
    answer = []
    for i in range(2, n+1):
        while n % i == 0:
            n //= i
            answer.append(i) if i not in answer else None
    return answer