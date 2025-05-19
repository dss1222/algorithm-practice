#https://school.programmers.co.kr/learn/courses/30/lessons/120848
import math
def solution(n):
    for i in range(11, 0, -1):
        if math.factorial(i) <= n:
            return i
        
def solution2(n):
    fact = 1
    i = 1
    while fact * (i + 1) <= n:
        print(f"i: {i}, fact: {fact}")
        i += 1
        fact *= i
    return i

print(solution2(1))
print(solution2(10))
