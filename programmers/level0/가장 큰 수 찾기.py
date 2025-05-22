#https://school.programmers.co.kr/learn/courses/30/lessons/120899
def solution(array):
    return [max(array), array.index(max(array))]

print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

# .index() : 인덱스를 찾는 함수