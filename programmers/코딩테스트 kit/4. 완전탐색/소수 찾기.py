#https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    for i in range(len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            nums.add(num)

    return sum(1 for num in nums if is_prime(num))


def get_prime_set(limit):
    is_prime = [False, False] + [True] * (limit - 1)
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*2, limit+1, i):
                is_prime[j] = False
    return set(i for i, prime in enumerate(is_prime) if prime)

def solution2(numbers):
    nums = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            nums.add(num)
    prime_set = get_prime_set(9999999)
    return sum(1 for num in nums if num in prime_set)

def solution3(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)