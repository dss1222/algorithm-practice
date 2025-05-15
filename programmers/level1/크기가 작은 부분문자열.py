#https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    length = len(p)
    t_list = []
    for i in range(len(t) - len(p) + 1):
        t_list.append(t[i:i+length])
    for i in range(len(t_list)):
        if int(t_list[i]) <= int(p):
            answer += 1 
    return answer

def ex_solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer

# 테스트
if __name__ == "__main__":
    print(solution("3141592", "271"))  # 2
    print(solution("500210", "10"))  # 2
    print(solution("10203", "15"))  # 3
