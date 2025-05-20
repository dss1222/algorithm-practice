#https://school.programmers.co.kr/learn/courses/30/lessons/120853
def solution(s):
    answer = 0
    data = s.split(" ")

    for i in range(len(data)):
        if data[i] == 'Z':
            answer -= int(data[i-1])
        else:
            answer += int(data[i])

    return answer

print(solution("1 2 Z 3"))
