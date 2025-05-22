#https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    for q in quiz:
        if eval(q.split("=")[0]) == int(q.split("=")[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))

def solution2(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(' = ')
        a,op,b = L.split()
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer