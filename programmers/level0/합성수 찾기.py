#https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i != 1 and not is_prime(i):
            answer += 1
    return answer

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution2(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

def solution3(n):
    # 0, 1은 소수가 아님
    is_prime = sieve(n)
    # 합성수는 1이 아니고, 소수가 아닌 수
    answer = 0
    for i in range(2, n + 1):
        if not is_prime[i]:
            answer += 1
    return answer

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime