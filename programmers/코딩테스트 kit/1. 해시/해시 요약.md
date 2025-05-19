
# 🔑 해시(Hash)란?

## ✅ 정의
해시는 데이터를 고유한 키에 매핑하여 **빠르게 검색, 삽입, 삭제할 수 있도록 만든 자료구조**입니다.  
코딩테스트에서는 주로 **딕셔너리(dict)** 또는 **집합(set)** 구조를 의미하며,  
복잡한 정렬 없이 **O(1)에 가까운 시간 복잡도로 데이터 탐색**이 가능하다는 장점이 있습니다.

---

## 🧠 왜 해시를 쓰는가?

| 상황 | 해시 사용 이유 |
|------|----------------|
| 특정 값이 있는지 빠르게 확인 | `if x in set()`은 평균 O(1) |
| 데이터의 출현 빈도 세기 | `Counter`, `dict[x] += 1` |
| 중복 제거 | `set()`으로 한 줄에 해결 |
| 키-값 매핑 | 이름, 아이디, 인덱스 등을 빠르게 연결

---

## 🛠 Python에서 자주 쓰는 해시 자료형

### 1. `dict`
키와 값을 1:1로 매핑할 수 있는 기본 해시 자료형입니다.  
탐색/삽입/삭제가 평균적으로 O(1)입니다.

```python
scores = {"철수": 90, "영희": 95}
scores["민수"] = 100  # 삽입
print(scores["영희"]) # 95
```

### 2. `set`
중복이 없는 값을 저장할 수 있는 해시 기반의 집합입니다.  
원소 존재 여부 확인 시 매우 빠릅니다.

```python
visited = set()
visited.add("node1")
print("node2" in visited)  # False
```

### 3. `collections.Counter`
리스트와 같은 반복 가능한 객체의 원소 등장 횟수를 자동으로 세줍니다.  
빈도 기반 문제에서 유용하게 사용됩니다.

```python
from collections import Counter
arr = ["a", "b", "a", "c"]
count = Counter(arr)
print(count["a"])  # 2
```

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 등장 횟수 세기 | Counter, dict[x] += 1 | [완주하지 못한 선수] |
| 중복 여부 확인 | `if x in set` | [전화번호 목록] |
| 조건 만족 쌍 찾기 | dict로 보완값 저장 | [두 수의 합] |
| 분류별 개수 누적 | `dict[분류] += 1` | [의상] |

---

## ⚠️ 실수 주의

- dict에서 키가 없을 경우 `KeyError` → `dict.get(key, 0)` 또는 `defaultdict(int)` 사용
- set은 중복을 자동 제거하지만 순서는 보장되지 않음
- Counter는 연산은 편하지만 덧셈/뺄셈 시 부작용 주의

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| 완주하지 못한 선수 | https://school.programmers.co.kr/learn/courses/30/lessons/42576 |
| 전화번호 목록 | https://school.programmers.co.kr/learn/courses/30/lessons/42577 |
| 의상 | https://school.programmers.co.kr/learn/courses/30/lessons/42578 |
| 베스트앨범 | https://school.programmers.co.kr/learn/courses/30/lessons/42579 |

---

## ⏱ 시간복잡도 요약

| 연산 | 평균 시간 복잡도 |
|------|------------------|
| 딕셔너리 삽입/탐색/삭제 | O(1) |
| 셋 삽입/탐색 | O(1) |
| Counter 생성 | O(N)

---

## 🧭 요약 정리

- 해시는 "빠르게 찾고, 세고, 매핑할 수 있는" 도구
- dict, set, Counter를 자유자재로 쓰는 연습 필요
- 많은 문제에서 **정렬보다 더 빠른 해시 접근**이 요구됨
