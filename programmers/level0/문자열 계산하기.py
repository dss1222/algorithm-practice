def solution(my_string):
    return eval(my_string)


def solution_example(my_string):
    tokens = my_string.split()
    print(tokens)
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = int(tokens[i+1])
        if op == '+':
            result += num
        else:
            result -= num
    return result

print(solution_example("3 + 4"))
