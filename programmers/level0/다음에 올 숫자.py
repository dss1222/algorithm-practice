#https://school.programmers.co.kr/learn/courses/30/lessons/120924
def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[2] / common[1])


    diff = common[1] - common[0]

    if common[0] != 0:
        ratio = common[1] / common[0]
    else:
        ratio = 0

    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + diff
    else:
        return common[-1] * ratio

if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
    print(solution([2, 4, 8]))
