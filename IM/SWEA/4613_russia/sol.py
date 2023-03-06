import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 1. 영역을 나눈다.
    # 흰 색 : 0~1, 파란 색 : 1~2, 빨간 색 : 2~3
    minV = 2500
    for a in range(N-2):
        for b in range(a+1, N-1):
            # 2. 영역 안에서 해당 색이 아닌 개수를 센다.
            cnt = 0
            for i in range(a + 1):  # 흰색 영역에서 다른 색의 개수 구함
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a+1, b+1):
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b+1, N):
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1
            if minV > cnt:
                minV = cnt
    print(f'#{tc} {minV}')
