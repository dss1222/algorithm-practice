#https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[i] * n
    return answer

# 테스트
if __name__ == "__main__":
    print(solution("hello", 3))  # "hhheeellllllooo"
    print(solution("hi", 2))  # "hhii"
