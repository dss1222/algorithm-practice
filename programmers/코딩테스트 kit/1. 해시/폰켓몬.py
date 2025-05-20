#https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter

def solution(nums):
    pick_count = len(nums) // 2
    nums_count = Counter(nums)

    if len(nums_count) > pick_count:
        return pick_count
    else:
        return len(nums_count)


print(solution([3,1,2,3]))

def solution2(ls):
    return min(len(ls)/2, len(set(ls)))