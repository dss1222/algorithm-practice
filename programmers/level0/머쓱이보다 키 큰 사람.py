#https://school.programmers.co.kr/learn/courses/30/lessons/120585
def solution(array, height):
    count = 0
    for i in array:
        if i > height:
            count += 1
    return count

print(solution([149, 180, 167, 192, 170], 167))

def solution_example(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)