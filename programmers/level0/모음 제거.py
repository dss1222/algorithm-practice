#https://school.programmers.co.kr/learn/courses/30/lessons/120849
def solution(my_string):
    data = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in my_string:
        if i not in data:
            answer += i


    return answer

def solution2(my_string):
    return ''.join([i for i in my_string if i not in 'aeiou'])

def solution3(my_string):
    vowles = ['a', 'e', 'i', 'o', 'u']
    for i in vowles:
        my_string = my_string.replace(i, '')
    return my_string
    
