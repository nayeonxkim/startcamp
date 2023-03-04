import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    # N개 중 K개의 합 중 가장 큰 값
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    # 모든 k개 성적 조합 생성
    A = list(combinations(score, K))

    # 모든 조합을 순회하며 그 합이 가장 큰 것을 반환
    max_total = 0
    for lst in A:
        if max_total < sum(lst):
            max_total = sum(lst)
    print(f'#{tc} {max_total}')