from collections import Counter

def solution(participant, completion):
    result = participant + completion
    count = Counter(result)

    for key, value in count.items():
        if value > 2 and value % 2 != 0:
            return key

        if value == 1:
            return key

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(solution2(["leo", "kiki", "eden"], ["eden", "kiki"]))


