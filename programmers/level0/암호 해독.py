#https://school.programmers.co.kr/learn/courses/30/lessons/120892
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer

def solution2(cipher, code):
    return cipher[code-1::code]
