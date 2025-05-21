from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()

    for i in range(len(progresses)):
        remain = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            remain += 1
        queue.append(remain)
    

    while queue:
        count = 0
        temp = queue[0]
        for i in range(len(queue)):
            queue[i] -= temp

        if queue:
            while queue and queue[0] <= 0:
                queue.popleft()
                count += 1
            if count > 0:
                answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

def solution_example(progresses, speeds):
    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        remain = (100 - p) // s
        if (100 - p) % s != 0:
            remain += 1
        days.append(remain)

    prev = days[0]
    count = 1
    for day in days[1:]:
        if day <= prev:
            count += 1
        else:
            answer.append(count)
            prev = day
            count = 1
    answer.append(count)
    return answer