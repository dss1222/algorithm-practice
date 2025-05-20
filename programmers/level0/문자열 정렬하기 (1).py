#https://school.programmers.co.kr/learn/courses/30/lessons/120850
def solution(my_string):
    answer = []
    [answer.append(int(i)) for i in my_string if i.isdigit()]
    answer.sort()
    return answer


def solution2(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])