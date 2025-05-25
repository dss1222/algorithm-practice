def solution(sides):
    max_side = max(sides)
    min_side = min(sides)

    side_list = []

    for i in range(max_side - min_side + 1, max_side + 1):
        side_list.append(i)
    for i in range(max_side + 1, max_side + min_side):
        side_list.append(i)
    return len(set(side_list))


def solution2(sides):
    return (sum(sides) - 1) - abs(sides[0] - sides[1])
