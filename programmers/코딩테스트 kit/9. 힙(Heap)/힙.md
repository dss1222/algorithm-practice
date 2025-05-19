
# ⛰ 힙(Heap)이란?

## ✅ 정의
힙은 **우선순위가 있는 데이터를 빠르게 꺼내기 위한 자료구조**입니다.  
항상 최댓값 또는 최솟값 중 하나를 빠르게 찾는 데 특화되어 있으며,  
코딩테스트에서는 주로 **우선순위 큐(Priority Queue)** 로 활용됩니다.

---

## 🧠 힙을 쓰는 이유

| 상황 | 사용 예시 |
|------|-----------|
| 가장 작은/큰 값을 빠르게 꺼내야 할 때 | 우선순위 큐 |
| 정렬된 순서대로 데이터를 꺼낼 때 | 힙 정렬 |
| 실시간으로 최솟값/최댓값 유지 | 스트리밍 데이터 처리 등 |
| Dijkstra, A*, 스케줄링 문제 등 | 최단 경로 알고리즘, 작업 순서 처리 등 |

---

## 🛠 Python에서 힙 사용하기 (`heapq`)

### 1. 기본 사용 (최소 힙: Min-Heap)
```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # 1 (가장 작은 값부터 나옴)
```

### 2. 최대 힙 구현 방법 (음수 변환)
Python 기본은 최소 힙이므로, 최대 힙은 값에 `-`를 붙여서 사용합니다.
```python
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)

print(-heapq.heappop(max_heap))  # 5
```

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 가장 작은 값부터 순차 꺼내기 | 최소 힙 | [더 맵게] |
| 가장 큰 값 우선 꺼내기 | 최대 힙 (음수 사용) | [이중우선순위큐] |
| 정렬된 순서 유지 | 힙 정렬 느낌 | [디스크 컨트롤러] |
| K번째 큰 수 찾기 | 고정 크기 힙 유지 | heapq 활용 |

---

## ⚠️ 실수 주의

- `heapq`는 리스트를 직접 힙처럼 다룸 → `heapq.heapify(list)` 필요
- 최대 힙은 `-값` 삽입/추출 방식 외엔 직접 구현해야 함
- 값 비교 기준이 커스텀일 경우 `(우선순위, 값)` 튜플 사용

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) |
| [디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627) |
| [이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) |

---

## ⏱ 시간복잡도 요약

| 연산 | 시간 복잡도 |
|------|---------------|
| 삽입 (`heappush`) | O(log N) |
| 삭제 (`heappop`) | O(log N) |
| 최솟값 조회 | O(1) |

---

## 🧭 요약 정리

- 힙은 "우선순위 있는 데이터 처리"에 특화된 구조
- Python 기본은 **최소 힙**, 최대 힙은 `-값` 변환
- `heapq` 모듈을 통한 리스트 기반 사용
- 효율적인 정렬/우선순위 문제에서 자주 등장
