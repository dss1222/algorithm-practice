#https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    for size in sizes:
        size.sort()
    
    max_width = 0
    max_height = 0
        
    for size in sizes:
        if size[0] > max_width:
            max_width = size[0]
        if size[1] > max_height:
            max_height = size[1]
        
    return max_width * max_height

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

def solution2(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col