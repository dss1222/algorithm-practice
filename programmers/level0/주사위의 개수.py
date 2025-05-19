#https://school.programmers.co.kr/learn/courses/30/lessons/120845
def solution(box, n):
    가로개수 = box[0] // n
    세로개수 = box[1] // n
    높이개수 = box[2] // n
    return 가로개수 * 세로개수 * 높이개수