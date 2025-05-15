# https://school.programmers.co.kr/learn/courses/30/lessons/120822
def solution(num_list):
    return num_list[::-1]

def solution2(num_list):
    return list(reversed(num_list))

def solution3(num_list):
    num_list.reverse()
    return num_list

# 테스트
if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
    print(solution([1, 2, 3, 4, 5, 6]))  # [6, 5, 4, 3, 2, 1]
    print(solution([1, 1, 1, 1, 1]))  # [1, 1, 1, 1, 1]

