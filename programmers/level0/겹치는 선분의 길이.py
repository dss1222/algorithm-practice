#https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    arr = [0] * 201
    for start, end in lines:
        for i in range(start, end):
            arr[i+100] += 1
            
    return sum(1 for i in arr if i > 1)