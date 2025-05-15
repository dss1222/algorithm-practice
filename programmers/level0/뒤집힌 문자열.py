#https://school.programmers.co.kr/learn/courses/30/lessons/120822
def solution(my_string):
    return my_string[::-1]

# 테스트
if __name__ == "__main__":
    print(solution("hello"))  # "olleh"
    print(solution("programmers"))  # "sretcarahcimreh"
    print(solution(""))  # ""


