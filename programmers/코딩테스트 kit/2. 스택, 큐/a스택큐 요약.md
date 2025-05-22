
# 📚 스택/큐란?

## ✅ 정의

- **스택(Stack)**: LIFO(Last-In-First-Out), 마지막에 들어간 데이터가 가장 먼저 나오는 구조
- **큐(Queue)**: FIFO(First-In-First-Out), 먼저 들어간 데이터가 먼저 나오는 구조

둘 다 기본적인 선형 자료구조이며, 순서 제어, 상태 추적, 순차 처리 등에 널리 사용됩니다.  
코딩테스트에서는 **시뮬레이션, 순서 처리, 문제 해결 순서 추적** 등에 자주 활용됩니다.

---

## 🧠 왜 스택/큐를 쓰는가?

| 상황 | 사용 예시 |
|------|------------|
| 함수 호출 추적, 괄호 짝 검사 | 스택 |
| 프로세스 순서, 프린터 대기열 | 큐 |
| 순차적으로 진행되는 처리 시뮬레이션 | 큐 |
| 상태 저장/복원, 되돌리기 | 스택 |

---

## 🛠 Python에서 자주 쓰는 스택/큐 방법

### 1. `list` 기반 스택
```python
stack = []
stack.append(1)    # push
stack.pop()        # pop (마지막 원소 반환)
```

### 2. `collections.deque` 기반 큐
```python
from collections import deque

queue = deque()
queue.append(1)        # enqueue
queue.popleft()        # dequeue
```

> 💡 `deque`는 양쪽 삽입/삭제가 O(1)로 빠르며 큐 구현 시 필수

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 괄호 짝 검사 | 여는 괄호 push → 닫는 괄호와 매칭 pop | [올바른 괄호] |
| 프린터 문제 | 우선순위 있는 큐 시뮬레이션 | [프린터] |
| 기능개발 시뮬 | 스택처럼 누적 처리 | [기능개발] |
| 다리를 지나는 트럭 | 조건에 따라 큐 상태 시뮬 | [다리를 지나는 트럭] |

---

## ⚠️ 실수 주의

- `list.pop(0)`은 느림 → 큐는 `deque.popleft()` 사용
- `stack[-1]`로 peek 가능, 비었는지 먼저 확인
- 스택/큐 상태 변화는 반복문 시뮬레이션과 함께 쓰는 경우 많음

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) |
| [프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587) |
| [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909) |
| [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583) |

---

## ⏱ 시간복잡도 요약

| 연산 | list | deque |
|------|------|-------|
| push / append | O(1) | O(1) |
| pop (끝) | O(1) | O(1) |
| pop(0) | ❌ O(N) | ✅ O(1) with popleft |

---

## 🧭 요약 정리

- 스택은 "쌓고 빼는", 큐는 "밀고 당기는" 구조
- 시뮬레이션 문제에서 빈번히 등장
- `deque`를 사용해 성능 확보
