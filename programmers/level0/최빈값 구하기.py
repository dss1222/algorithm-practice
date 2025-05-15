# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from collections import Counter

def solution(array):
    counter = Counter(array)
    most_common = counter.most_common()

    print(f"counter: {counter}")
    print(f"most_common: {most_common}")

    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    return most_common[0][0]

# 테스트
if __name__ == "__main__":
    print(solution([1, 2, 3, 3, 3, 4]))  # 3
    print(solution([1, 1, 2, 2]))  # -1
    print(solution([1]))  # 1

