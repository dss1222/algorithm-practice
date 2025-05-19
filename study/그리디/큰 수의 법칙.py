def solution(n, m, k, data):
    count = 0
    data.sort()
    first = data[-1]
    second = data[-2]
    answer = 0
    for i in range(1, m+1):
        if count < k:
            answer += first
            count += 1
        else:
            answer += second
            count = 0
    return answer

print(solution(5, 8, 3, [2, 4, 5, 4, 6])) # 46

def solution_example():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first = data[-1]
    second = data[-2]

    result = 0

    while True:
        for i in range(k): # 가장 큰 수를 k번 더하기
            if m == 0: # m이 0이라면 반복문 탈출
                break
            result += first
            m -= 1 # 더할 때마다 1씩 빼기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += second # 두 번째로 큰 수를 한 번 더하기
        m -= 1 # 더할 때마다 1씩 빼기
    print(result)

def solution_example2():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first = data[-1]
    second = data[-2]

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m / (k+1)) * k
    count += m % (k+1)

    result = 0
    result += count * first # 가장 큰 수 더하기
    result += (m - count) * second # 두 번째로 큰 수 더하기

    print(result)

solution_example2()
