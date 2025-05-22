#https://school.programmers.co.kr/learn/courses/30/lessons/120906
def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k)) + 1

    else:
        return -1


print(solution(29183, 1))
print(solution(123456, 7))
