
# 📐 동적 계획법(DP, Dynamic Programming)이란?

## ✅ 정의
동적 계획법(DP)은 **큰 문제를 작은 문제로 나누고**,  
작은 문제의 정답을 **한 번만 구해 저장(Memoization)** 하여  
**중복 계산을 줄이는 알고리즘 설계 기법**입니다.

---

## 🧠 언제 DP를 쓰는가?

| 조건 | 설명 |
|------|------|
| **작은 문제들이 반복해서 나타남** | Overlapping Subproblems |
| **작은 문제의 정답이 큰 문제 해결에 사용됨** | Optimal Substructure |
| **재귀로 풀면 중복 계산이 심함** | → 메모이제이션 필요 |
| **최댓값/최솟값/방법 수 구하기 문제** | 대표적인 DP 문제

> 💡 큰 문제를 쪼개고, 풀었던 문제는 다시 풀지 않도록 "기억"하면 된다!

---

## 🛠 Python 구현 방식

### 1. Bottom-Up (반복문)
```python
dp = [0] * 100
dp[0] = 1
dp[1] = 1
for i in range(2, 100):
    dp[i] = dp[i-1] + dp[i-2]
```

### 2. Top-Down (재귀 + Memoization)
```python
def fib(n, memo={}):
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## 📚 자주 나오는 패턴

| 패턴 | 설명 | 예시 |
|------|------|------|
| 피보나치 수열 | 가장 기본적인 DP 구조 | [피보나치 수] |
| 최소 비용 문제 | 앞에서 계산된 최솟값 기반 누적 | [정수 삼각형] |
| 경우의 수 누적 | 특정 조건에서 올 수 있는 경로 누적 | [N으로 표현] |
| 배낭 문제 (Knapsack) | 조건을 만족하는 최대/최소 | [카드 구매하기] |
| 문자열 비교 | 편집 거리, 공통 부분 수열 | [LCS, Levenshtein 거리] |

---

## ⚠️ 실수 주의

- DP 테이블 초기화 제대로 하기
- 점화식 확인: 인덱스 범위, off-by-one 오류 주의
- 메모이제이션 시 key 캐싱 제대로 하기
- Top-down은 재귀 깊이 제한 고려 필요

---

## 📌 추천 문제 (프로그래머스 고득점 Kit)

| 문제 | 링크 |
|------|------|
| [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) |
| [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) |
| [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) |
| [도둑질](https://school.programmers.co.kr/learn/courses/30/lessons/42897) |

---

## ⏱ 시간복잡도 요약

| 구조 | 시간 복잡도 |
|------|---------------|
| 1차원 DP | O(N) |
| 2차원 DP | O(N * M) |
| Top-down (메모이제이션) | 중복 제거 시 O(N) |
| 일반 재귀 (비추천) | O(2^N) → 중복 호출 발생

---

## 🧭 요약 정리

- DP는 "기억하며 푸는 알고리즘"
- Bottom-Up은 반복문, Top-Down은 재귀 + memo
- **점화식, 초기값, 조건 정의**가 핵심
- 반복 구조 파악 + 메모 테이블 설계 연습이 중요
