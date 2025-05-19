
# 🎯 이분 탐색(Binary Search)이란?

## ✅ 정의
이분 탐색은 **정렬된 배열**을 반으로 나누며 원하는 값을 빠르게 찾는 탐색 알고리즘입니다.  
**탐색 범위를 절반씩 줄이므로** 시간 복잡도가 O(log N)으로 매우 효율적입니다.

---

## 🧠 언제 이분 탐색을 쓰는가?

| 상황 | 설명 |
|------|------|
| 배열이 정렬되어 있을 때 | 기본 조건 |
| 특정 값의 존재 여부 | 탐색용 |
| 특정 조건을 만족하는 값의 범위 찾기 | "최솟값/최댓값" 문제 |
| 범위 내 최적값을 구하는 문제 | 파라메트릭 서치 방식 |

---

## 🛠 Python 구현 방법

### 1. 기본 이분 탐색
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 2. bisect 모듈 사용
```python
import bisect

arr = [1, 2, 4, 4, 5]
idx = bisect.bisect_left(arr, 4)  # 4가 처음 등장하는 위치
```

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 값의 존재 여부 탐색 | 단순 탐색 | [입국심사] |
| 가장 짧은 길이 / 최소 최대값 | 파라메트릭 서치 | [징검다리 건너기] |
| 조건을 만족하는 최소값 찾기 | 이분탐색으로 범위 줄이기 | [예산 문제] |
| 중복 원소 구간 찾기 | `bisect_left`, `bisect_right` 활용 | [숫자 카드 2] |

---

## ⚠️ 실수 주의

- **정렬된 배열이어야 함**
- mid 계산 시 `left + (right - left) // 2` 형식을 추천
- `bisect_left`, `bisect_right`의 차이점 숙지
- 무한 루프 or off-by-one 오류 주의

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) |
| [예산](https://school.programmers.co.kr/learn/courses/30/lessons/43237) |
| [징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236) |

---

## ⏱ 시간복잡도 요약

| 방식 | 시간 복잡도 |
|------|---------------|
| 단순 이분 탐색 | O(log N) |
| 파라메트릭 서치 | O(log(max값) * N) |
| bisect 모듈 | O(log N)

---

## 🧭 요약 정리

- 이분 탐색은 "정렬된 배열에서 절반씩 줄이며 탐색"하는 방식
- 값 탐색, 조건 만족 최솟값/최댓값 찾기에 유용
- **문제에서 범위 조정 조건이 보이면** 이분 탐색 의심!
