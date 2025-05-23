def solution(citations):
    citations.sort(reverse=True)

    for idx, citation in enumerate(citations):
        if idx + 1 > citation:
            return idx
        
    return len(citations)


print(solution([3, 0, 6, 1, 5]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def solution_count(citations):
    n = len(citations)
    max_cite = max(citations)
    counts = [0] * (max_cite + 2)  # +2는 인덱스 에러 방지

    # 인용 횟수별 논문 개수 세기
    for c in citations:
        if c > n:
            counts[n] += 1
        else:
            counts[c] += 1

    total = 0
    for h in range(n, -1, -1):
        total += counts[h]
        if total >= h:
            return h