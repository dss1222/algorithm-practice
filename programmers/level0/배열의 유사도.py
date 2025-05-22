from collections import Counter
def solution(s1, s2):
    s1_counter, s2_counter = Counter(s1), Counter(s2)
    s1_counter.update(s2_counter)
    answer = 0
    for i in s1_counter.keys():
        if s1_counter[i] > 1:
            answer += 1

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))

def solution2(s1, s2):
    return len(set(s1)&set(s2))