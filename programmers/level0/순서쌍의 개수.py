#https://school.programmers.co.kr/learn/courses/30/lessons/120836
def solution(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1  # 제곱수인 경우 (10, 10)처럼 한 번만 카운트
            else:
                count += 2  # (i, n//i), (n//i, i) 두 쌍
    return count

    if __name__ == "__main__":
        print(solution(20))
        print(solution(100))