
# 🔍 완전탐색(Brute Force)이란?

## ✅ 정의
완전탐색은 가능한 모든 경우의 수를 **전부 탐색**해서 답을 찾는 방식입니다.  
단순하고 직관적이지만, 경우의 수가 많아지면 **비효율적**일 수 있어 **시간복잡도 고려**가 중요합니다.

---

## 🧠 왜 완전탐색을 쓰는가?

| 상황 | 사용 예시 |
|------|-----------|
| 가능한 선택이 적고 명확한 경우 | 1~9 중 비밀번호 조합 찾기 |
| 모든 조합/순열을 다 확인해야 하는 경우 | 모의고사 정답 비교, 숫자 야구 |
| 가장 간단하고 안전한 시작점이 필요한 경우 | 제한이 작을 때 기본 접근 |

> 💡 제한이 작고 (예: N ≤ 10), 최적화 필요 없을 때 완전탐색으로 푸는 게 가장 쉬움

---

## 🛠 완전탐색 구현 방식

### 1. `for` 중첩 루프 (단순 반복)
```python
for i in range(10):
    for j in range(10):
        print(i, j)
```

### 2. `itertools.permutations` (순열)
```python
from itertools import permutations
for p in permutations([1, 2, 3], 2):
    print(p)  # (1, 2), (1, 3), ...
```

### 3. `itertools.combinations` (조합)
```python
from itertools import combinations
for c in combinations([1, 2, 3], 2):
    print(c)  # (1, 2), (1, 3), ...
```

### 4. 재귀 기반 백트래킹
```python
def dfs(path):
    if len(path) == 3:
        print(path)
        return
    for i in range(1, 4):
        dfs(path + [i])

dfs([])
```

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 순열 | 가능한 모든 순서를 탐색 | [모의고사] |
| 조합 | 선택 가능한 모든 조합 탐색 | [소수 만들기] |
| DFS 기반 백트래킹 | 조건에 따라 탐색 가지치기 | [전력망을 둘로 나누기] |
| N자리 수열 생성 | 반복 or 재귀로 구현 | [카펫], [숫자 야구] |

---

## ⚠️ 실수 주의

- 시간복잡도 체크 필수: N이 커질수록 폭발적으로 증가
- 중복 탐색이 필요한지 / 제거해야 하는지 확인
- `itertools`는 외워두면 구현 생략 가능

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840) |
| [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977) |
| [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) |
| [숫자 야구](https://school.programmers.co.kr/learn/courses/30/lessons/42841) |

---

## ⏱ 시간복잡도 요약

| 탐색 유형 | 시간 복잡도 |
|-----------|---------------|
| N중 for문 | O(N^k) |
| 순열 (`permutations`) | O(N!) |
| 조합 (`combinations`) | O(NCr) |
| DFS/백트래킹 | 문제 구조에 따라 다양 (보통 O(2^N) 이상 가능성)

---

## 🧭 요약 정리

- 완전탐색은 "가능한 모든 경우를 시도"하는 가장 기본적인 접근
- 조합, 순열, 백트래킹은 완전탐색의 핵심 도구
- **작은 범위 문제엔 최적**, 크면 시간초과 방지 전략 병행 필요
