# https://school.programmers.co.kr/learn/challenges/beginner?order=recent&languages=python3
def solution(num_list):
    even = 0
    odd = 0
    for n in num_list:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

# 테스트
if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))  # [2, 3]
    print(solution([1, 3, 5, 7]))  # [0, 4]
    print(solution([2, 4, 6, 8, 10]))  # [5, 0]

