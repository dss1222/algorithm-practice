# https://school.programmers.co.kr/learn/courses/30/lessons/120830
def solution(n, k):
    sale_count = n // 10
    answer = n * 12000 + (k - sale_count) * 2000
    return answer

def solution2(n, k):
    service = n//10
    drink = max(0, k-service)
    return (12000*n)+(2000*drink)