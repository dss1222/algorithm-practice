#https://school.programmers.co.kr/learn/courses/30/lessons/120889
def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2

print(solution([1, 2, 3]))

def solution2(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2