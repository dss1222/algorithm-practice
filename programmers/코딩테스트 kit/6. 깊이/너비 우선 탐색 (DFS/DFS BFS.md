
# 🌊 깊이/너비 우선 탐색 (DFS / BFS)이란?

## ✅ 정의

- **DFS (Depth-First Search)**: 깊이 우선 탐색. 한 방향으로 갈 수 있을 때까지 깊게 들어간 뒤, 더 이상 갈 수 없을 때 이전으로 되돌아가며 탐색  
- **BFS (Breadth-First Search)**: 너비 우선 탐색. 현재 노드의 이웃들을 먼저 모두 탐색한 뒤, 그 다음 깊이로 이동하는 방식

둘 다 **그래프 탐색 알고리즘**의 대표로, **그래프, 트리, 맵, 미로, 경로 찾기 문제**에서 자주 사용됩니다.

---

## 🧠 언제 DFS / BFS를 쓰는가?

| 상황 | DFS | BFS |
|------|-----|-----|
| **경로의 모든 경우 탐색** | ✅ | ❌ |
| **최단 거리 탐색** | ❌ | ✅ |
| **재귀 구조에 익숙할 때** | ✅ | ❌ |
| **큐를 통한 레벨 단위 탐색** | ❌ | ✅ |

---

## 🛠 Python 구현 방법

### DFS - 재귀 방식
```python
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

### DFS - 스택 방식
```python
def dfs_stack(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(reversed(graph[node]))
```

### BFS - 큐 방식
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
```

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 미로 탐색 | BFS로 최단 경로 탐색 | [미로 탈출] |
| 섬의 개수 | DFS로 연결된 영역 카운트 | [네트워크] |
| 단지번호붙이기 | DFS/BFS 모두 가능 | [단지번호붙이기] |
| 특정 조건의 영역 확장 | DFS로 조건 따라 탐색 | [타겟 넘버], [게임 맵 최단거리] |

---

## ⚠️ 실수 주의

- DFS 재귀는 **`sys.setrecursionlimit()`** 필요할 수 있음
- BFS는 큐를 반드시 `deque`로 사용 → `pop(0)`은 느림
- 방문처리 (`visited`)를 **언제 어떻게 하는지** 주의
- DFS는 **순서에 따라 결과가 달라질 수 있음**

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) |
| [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) |
| [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) |
| [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) |

---

## ⏱ 시간복잡도 요약

| 기준 | DFS | BFS |
|------|-----|-----|
| 그래프 탐색 | O(V + E) | O(V + E) |
| 최단 거리 | ❌ | ✅ |
| 경로 수 탐색 | ✅ | ❌ |

---

## 🧭 요약 정리

- DFS는 "끝까지 파고들기", BFS는 "넓게 퍼지기"
- **DFS: 경로의 모든 경우** 탐색에 적합
- **BFS: 최단 거리** 문제에 최적
- 방문 처리 위치/순서 주의, `deque`, 재귀 깊이 고려
