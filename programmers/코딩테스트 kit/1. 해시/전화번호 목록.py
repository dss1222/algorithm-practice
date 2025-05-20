#https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

def solution2(phone_book):
    answer = True
    hash_map = {phone_number:1 for phone_number in phone_book}
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer

print(solution2(["119", "97674223", "1195524421"]))
print(solution2(["123","456","789"]))
print(solution2(["12","123","1235","567","88"]))
