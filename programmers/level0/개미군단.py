#https://school.programmers.co.kr/learn/courses/30/lessons/120837
def solution(hp):
    answer = 0

    answer += hp // 5
    hp = hp % 5

    answer += hp // 3
    hp = hp % 3

    answer += hp // 1
    hp = hp % 1

    return answer


def solution2(hp):
    answer = 0
    for ant in [5, 3, 1]:
        # divmod는 몫과 나머지를 반환하는 함수
        d, hp = divmod(hp, ant)
        answer += d
    return answer