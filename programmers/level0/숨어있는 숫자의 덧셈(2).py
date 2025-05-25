#https://school.programmers.co.kr/learn/courses/30/lessons/120864
def solution(my_string):
    temp = ""
    string_list = []
    answer = 0
    for i in my_string:
        if i.isdigit():
            temp += i
        else:
            if temp:
                string_list.append(temp)
                temp = ""   
    if temp:
        string_list.append(temp)
    for i in string_list:
        answer += int(i)
    return answer

print(solution("aAb1B2cC34oOp"))

def solution2(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())