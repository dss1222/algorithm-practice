from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque()
    time = 0
    while truck_weights or q:
        time += 1
        if q:
            for i in q:
                i[1] -= 1
            if q[0][1] == 0:
                q.popleft()
        
        if truck_weights:
            if sum([i[0] for i in q]) + truck_weights[0] <= weight and len(q) < bridge_length:
                q.append([truck_weights.pop(0), bridge_length])

    return time


def solution_example(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 위 상태(길이만큼 0으로 초기화)
    time = 0
    total_weight = 0
    truck_weights = deque(truck_weights)

    while bridge:
        time += 1
        out = bridge.popleft()
        total_weight -= out

        if truck_weights:
            # 다음 트럭이 올라갈 수 있으면
            if total_weight + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
                total_weight += t
            else:
                bridge.append(0)  # 트럭이 못 올라가면 0(빈 칸) 추가
        print(f"bridge: {bridge}")

    return time

print(solution_example(2, 10, [7,4,5,6]))
