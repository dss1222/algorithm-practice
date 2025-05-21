#https://school.programmers.co.kr/learn/courses/30/lessons/120894
def solution(numbers):
    data = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(data)):
        numbers = numbers.replace(data[i], str(i))
    return int(numbers)

def solution2(numbers):
    data = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key, value in data.items():
        numbers = numbers.replace(key, value)
    return int(numbers)
