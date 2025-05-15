#https://school.programmers.co.kr/learn/courses/30/lessons/120810 
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 테스트
if __name__ == "__main__":
    print(solution(3, 2))  # 3을 2로 나눈 나머지
    print(solution(10, 5))  # 10을 5로 나눈 나머지
