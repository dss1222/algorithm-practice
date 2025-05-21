from collections import deque

def solution(priorities, location):
    location_idx = location
    max_num = max(priorities)

    queue = deque([[idx, p] for idx, p in enumerate(priorities)])

    count = 0

    while True:
        if queue[0][1] == max_num:
            count += 1
            if queue[0][0] == location_idx:
                break
            queue.popleft()
            max_num = max(queue, key=lambda x: x[1])[1]

        else:
            queue.append(queue.popleft())

    return count

print(solution([1, 1, 9, 1, 1, 1], 0))

def solution_example(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    priorities_sorted = sorted(priorities, reverse=True)
    count = 0
    i = 0

    while queue:
        idx, priority = queue.popleft()
        if priority == priorities_sorted[i]:
            count += 1
            i += 1
            if idx == location:
                return count
        else:
            queue.append((idx, priority))