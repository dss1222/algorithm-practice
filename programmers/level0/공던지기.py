#https://school.programmers.co.kr/learn/courses/30/lessons/120843
def solution(numbers, k):
    idx = 2 * (k - 1) % len(numbers)
    return numbers[idx]