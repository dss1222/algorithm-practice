# https://school.programmers.co.kr/learn/courses/30/lessons/120814
def solution(n):
    return n // 7 + 1 if n % 7 != 0 else n // 7

# 테스트
if __name__ == "__main__":
    print(solution(7))  # 1
    print(solution(1))  # 1
    print(solution(15))  # 3

