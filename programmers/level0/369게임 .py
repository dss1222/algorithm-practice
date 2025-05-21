#https://school.programmers.co.kr/learn/courses/30/lessons/120891
def solution(order):
    answer = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer

print(solution(29423))

def solution2(order):
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

# 문자열 관리 시 효율이 제일 좋음
def solution3(order):
    return sum(1 for i in str(order) if i in '369')

print(solution3(29423))
