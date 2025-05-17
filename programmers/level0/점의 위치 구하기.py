#https://school.programmers.co.kr/learn/courses/30/lessons/120841
def solution(dot):
    x, y = False, False
    if dot[0] > 0:
        x = True
    if dot[1] > 0:
        y = True
    
    if x and y:
        return 1
    elif x == False and y == True:
        return 2
    elif x == False and y == False:
        return 3
    else:
        return 4
    
def solution2(dot):
    x, y = dot
    if x * y > 0:
        return 1 if x > 0 else 3
    else:
        return 4 if x > 0 else 2

