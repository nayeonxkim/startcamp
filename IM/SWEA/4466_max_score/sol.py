import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N개 중 K개의 합 중 가장 큰 값
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse = True)

    max_total = 0
    for i in range(K):
        max_total += score[i]
    print(f'#{tc} {max_total}')