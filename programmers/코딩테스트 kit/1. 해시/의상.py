from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)

    for i in clothes:
        clothes_dict[i[1]] += 1

    answer = 1

    for key, value in clothes_dict.items():
        answer *= (value + 1)
    return answer - 1
    


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["crow_mask", "face"], ["blue_sunglasses", "face"]]))
