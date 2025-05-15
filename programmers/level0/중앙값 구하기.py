#https://school.programmers.co.kr/learn/courses/30/lessons/120811
def solution(array):
    array.sort()
    idx = len(array) // 2
    return array[idx]

# 테스트
if __name__ == "__main__":
    print(solution([1, 2, 7, 10, 11]))  # 7
    print(solution([9, -1, 0]))  # 0

