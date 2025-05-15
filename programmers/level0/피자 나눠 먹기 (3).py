#https://school.programmers.co.kr/learn/courses/30/lessons/120816
def solution(slice, n):
    return n // slice + 1 if n % slice != 0 else n // slice

# 테스트
if __name__ == "__main__":
    print(solution(7, 10))  # 2
    print(solution(4, 12))  # 3
