from functools import cmp_to_key

def compare(a, b):
    # 두 수를 문자열로 이어붙였을 때 더 큰 쪽이 앞으로 오도록
    if a + b > b + a:
        return -1  # a가 앞
    elif a + b < b + a:
        return 1   # b가 앞
    else:
        return 0

def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    # 커스텀 비교 함수로 정렬
    numbers.sort(key=cmp_to_key(compare))
    # 0이 여러 개일 때 "000..."이 되는 것 방지
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)

print(solution([6, 10, 2]))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))