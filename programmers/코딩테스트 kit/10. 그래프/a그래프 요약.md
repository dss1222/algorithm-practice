
# 🕸 그래프(Graph)란?

## ✅ 정의
그래프는 **정점(Vertex)**과 **간선(Edge)**으로 구성된 자료구조로,  
정점 간의 연결 관계를 표현하는 데 사용됩니다.  
현실 세계의 **길찾기, 네트워크, 연결 구조** 등을 모델링할 때 자주 등장합니다.

---

## 📌 그래프의 종류

| 유형 | 설명 |
|------|------|
| 방향 그래프 | 간선에 방향이 있음 (A → B) |
| 무방향 그래프 | 간선에 방향이 없음 (A — B) |
| 가중치 그래프 | 간선에 비용/길이 등의 값이 있음 |
| 연결 그래프 | 모든 정점이 하나의 연결 요소에 포함됨 |
| 비연결 그래프 | 일부 정점은 연결되지 않음 |

---

## 🧠 그래프 표현 방식

### 1. 인접 리스트 (가장 자주 사용됨)
```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
```

### 2. 인접 행렬
```python
graph = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
```

> 💡 노드 수가 많고 연결이 적을 땐 인접 리스트가 효율적

---

## 📚 자주 나오는 그래프 알고리즘

| 알고리즘 | 설명 | 예시 |
|----------|------|------|
| DFS / BFS | 그래프 순회 | [네트워크], [단지번호붙이기] |
| 유니온 파인드 | 서로소 집합 확인 | [사이클 판별], [크루스칼 MST] |
| 다익스트라 | 가중치 그래프의 최단 경로 | [최단 경로 문제] |
| 플로이드 워셜 | 모든 쌍 간의 최단 경로 | [경로 존재 여부] |
| 위상 정렬 | 순서가 있는 작업 정렬 | [과제 순서] |

---

## 🛠 그래프 기본 구현 예시

### 1. DFS (재귀)
```python
def dfs(graph, v, visited):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(graph, next, visited)
```

### 2. BFS (큐)
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
```

---

## ⚠️ 실수 주의

- 방문 처리 위치 주의 (`방문 전`, `큐 삽입 시점` 등)
- 방향/무방향 여부에 따라 간선 설정 달라짐
- 인접 행렬은 노드 수가 많으면 메모리 낭비

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) |
| [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) |
| [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) |
| [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) |

---

## ⏱ 시간복잡도 요약

| 방식 | 시간 복잡도 |
|------|---------------|
| DFS / BFS | O(V + E) |
| 인접 리스트 | O(V + E) |
| 인접 행렬 | O(V^2) |
| 다익스트라 (힙 사용) | O((V + E) log V)

---

## 🧭 요약 정리

- 그래프는 "연결 관계"를 표현하는 핵심 구조
- DFS/BFS를 통해 탐색, 유니온 파인드/다익스트라 등 알고리즘 다양
- 문제에 맞는 표현법(리스트/행렬) 선택과 방문 처리 방식이 핵심
