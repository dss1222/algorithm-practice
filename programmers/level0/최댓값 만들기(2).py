#https://school.programmers.co.kr/learn/courses/30/lessons/120862
def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer = max(answer, numbers[i]*numbers[j])
    return answer

def solution_answer(numbers):
    answer = 0
    answer_list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer_list.append(numbers[i]*numbers[j])
    return max(answer_list)


def solution2(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 