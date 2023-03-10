'''
어떤 집합의 부분집합 중에서
그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지 확인하는 문제

예를 들어 [-7, -3, -2, 5, 8] 집합이 있을 때,
[-3, -2, 5]는 이 집합의 부분집합이면서 합이 0이므로 답은 True가 된다.
---
# 완전검색
모든 부분집합을 생성하여 각 부분집합의 합을 계산한다.
-> 난이도가 낮은 문제. 시간제한이 긴 경우

## 먼저 부분집합을 생성하자
- 집합의 원소가 n개 일 때, 공집합을 포함한 부분집합의 수는 2**n개
- [1, 2, 3, 4] 집합
[0, 0, 0, 1] -> {4}
[0, 0, 1, 0] -> {3}
[0, 0, 1, 1] -> {3, 4}
---
'''

A = [1, 2, 3, 4]
bit = [0] * 4
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit, end = ' ')
                for p in range(4):
                    if bit[p]:
                        print(A[p], end = ' ')
                print()