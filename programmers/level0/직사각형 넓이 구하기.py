#https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    x_list = []
    y_list = []
    for dot in dots:
        x_list.append(dot[0])
        y_list.append(dot[1])
    answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
    return answer

def solution2(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])