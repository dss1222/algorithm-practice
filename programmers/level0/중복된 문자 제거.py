#https://school.programmers.co.kr/learn/courses/30/lessons/120888
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

print(solution("people"))

def solution2(my_string):
    return ''.join(dict.fromkeys(my_string))

#dict.fromkeys(iterable) : 중복된 요소를 제거하고 새로운 딕셔너리를 반환
#동일한 키는 무시하고, 처음 등장하는 키만 유지, 3.7 부터는 삽입 순서 유지
