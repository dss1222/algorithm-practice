#https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    age_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    answer = ''
    for i in str(age):
        answer += age_list[int(i)]
    return answer

if __name__ == "__main__":
    print(solution(23))
    print(solution(51))