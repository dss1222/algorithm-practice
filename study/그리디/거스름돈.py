def solution(n):
    coin_500 = n // 500
    coin_100 = (n % 500) // 100
    coin_50 = (n % 100) // 50
    coin_10 = (n % 50) // 10
    return coin_500 + coin_100 + coin_50 + coin_10

print(solution(1260))

def solution_example(n):
    # 시간 복잡도 O(N)
    coin_types = [500, 100, 50, 10]
    count = 0
    for coin in coin_types:
        count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
        n %= coin # 거슬러 준 만큼 금액 변경
    return count

print(solution_example(1260))
