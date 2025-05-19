def solution():
    n = int(input())
    answer = 0
    first = int(str(n)[0])
    for i in str(n):
        i = int(i)
        if i == 0 or i == 1 or i == first:
            answer += i
        else:
            answer *= i
    print(answer)

if __name__ == "__main__":
    solution()

def solution_example():
    data = input()
    result = int(data[0])
    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)
