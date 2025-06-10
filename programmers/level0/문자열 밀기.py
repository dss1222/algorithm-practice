def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]
    return -1

from collections import deque

def solution2(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1

print(solution2("hello", "ohell"))
print(solution2("apple", "elppa"))
print(solution2("atat", "tata"))
print(solution2("abc", "abc"))