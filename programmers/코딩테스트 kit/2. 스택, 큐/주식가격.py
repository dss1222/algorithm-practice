def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # 스택에 있는 인덱스들의 가격보다 현재 가격이 떨어지면
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 끝까지 남은 인덱스는 끝까지 가격이 떨어지지 않은 것
    for j in stack:
        answer[j] = len(prices) - 1 - j

    return answer

print(solution([1, 2, 3, 2, 3]))