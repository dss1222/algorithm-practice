def solution():
    n, m = map(int, input().split())
    result = 0
    # 한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(result, min_value)
    print(result)

def solution_example():
    n, m = map(int, input().split())
    result = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        result = max(result, min_value)
    print(result)
