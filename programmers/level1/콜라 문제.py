#https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    answer = 0
    # a 는 가져가는 개수 b는 주는 개수 n 은 처음 내가 가져온 개수
    while n >= a:
        new_cola = (n // a) * b
        answer += new_cola
        n = n % a + new_cola

    return answer

print(solution(2, 1, 20))
