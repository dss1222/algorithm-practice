#https://school.programmers.co.kr/learn/courses/30/lessons/120896
from collections import Counter

def solution(s):
    data = Counter(s)
    answer = ''
    for key, value in data.items(): 
        if value == 1:
            answer += key
    return ''.join(sorted(answer))

def solution2(s):
    return ''.join(sorted([i for i in s if s.count(i) == 1])
    )
