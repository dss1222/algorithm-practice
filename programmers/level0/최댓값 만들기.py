#https://school.programmers.co.kr/learn/courses/30/lessons/120847
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

def solution2(numbers):
    first = max(numbers)
    numbers.remove(first)
    second = max(numbers)
    return first * second