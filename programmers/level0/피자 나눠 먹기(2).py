#https://school.programmers.co.kr/learn/courses/30/lessons/120815
import math

def solution(n):
    lcm = math.lcm(6, n)
    return lcm//6

# 프로그래머스에선 python 3.8 이하인듯 함. lcm 함수가 없음
def solution_test(n):
    def lcm(a, b):
        return a * b // math.gcd(a, b)

    return lcm(6, n) // 6

# 테스트
if __name__ == "__main__":
    print(solution(6))  # 1
    print(solution(10))  # 5
    print(solution(4))  # 2

