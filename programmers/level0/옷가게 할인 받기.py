#https://school.programmers.co.kr/learn/courses/30/lessons/120818
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return int(price)

# 테스트
if __name__ == "__main__":
    print(solution(150000))  # 120000
    print(solution(580000))  # 464000
    print(solution(1000000))  # 800000

