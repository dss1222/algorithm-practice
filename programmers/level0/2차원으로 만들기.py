#https://school.programmers.co.kr/learn/courses/30/lessons/120842
def solution(num_list, n):
    answer = []
    mini_answer = []
    cnt = n
    for i in num_list:
        if cnt > 0:
            mini_answer.append(i)
            cnt -= 1
        else:
            cnt = n
            answer.append(mini_answer)
            mini_answer = []
            mini_answer.append(i)
            cnt -= 1
        if i == num_list[-1]:
            answer.append(mini_answer)

    return answer

def solution2(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
