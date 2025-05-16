#https://school.programmers.co.kr/learn/courses/30/lessons/120835
def solution(emergency):
    answer1 = []
    answer2 = []
    
    answer2 = sorted(emergency)
    answer2.reverse()

    for i in emergency:
        answer1.append(answer2.index(i)+1)
    return answer1


if __name__ == "__main__":
    print(solution([3, 76, 24])) # [3, 1, 2]
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(solution([30, 10, 23, 6, 100])) # [2, 4, 3, 5, 1]