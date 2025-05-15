#https://school.programmers.co.kr/learn/courses/30/lessons/120819
def solution(money):
    return [money // 5500, money % 5500]

# 테스트
if __name__ == "__main__":
    print(solution(5500))  # [1, 0]
    
