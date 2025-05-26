#https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    a, b, c, d = dots
    
    def slope(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:
            return 'inf'
        return dy / dx
    
    if slope(a, b) == slope(c, d):
        return 1
    if slope(a, c) == slope(b, d):
        return 1
    if slope(a, d) == slope(b, c):
        return 1
    
    return 0

def solution_example(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0