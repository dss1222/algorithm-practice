def solution(food):
    answer = "0" * food[0]
    food_count = []
    idx_count = len(food) - 1

    for i in range(1, len(food)):
        food_count.append(food[i]//2)

    food_count.reverse()

    for j in food_count:
        answer = str(idx_count) * j + answer + str(idx_count) * j
        idx_count -= 1


    return answer

def solution2(food):
    answer = ''
    for i, n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]

if __name__ == "__main__":
    print(solution([1, 3, 4, 6]))
    print(solution([1, 7, 1, 2]))