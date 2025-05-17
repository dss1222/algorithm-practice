#https://school.programmers.co.kr/learn/courses/30/lessons/120839
def solution(rsp):
    answer = ''
    answer_dict = {'2': '0', '0': '5', '5': '2'}
    for i in rsp:
        answer += answer_dict[i]

    return answer

def solution2(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)