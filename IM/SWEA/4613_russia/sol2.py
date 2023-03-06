import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        print(arr[i])
    # 영역의 범위를 조절하면서 바꿔야하는 칸의 개수를 센다.
    # 전체 행 : 0 ~ N-1행
    # 흰 색 : 0번 행 ~ N-3행까지 가능
    # 파란 색 : 흰색의 다음 행 ~ N-2행까지 가능
    # 빨간 색 : 파란색의 다음 행 ~ N-1행까지 가능
    min_cnt = 2500
    for w in range(N-2):
        for b in range(w+1, N-1):
            cnt = 0

            for i in range(w+1):
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1

            for i in range(w+1, b+1):
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1

            for i in range(b+1, N):
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1

            if min_cnt > cnt:
                min_cnt = cnt

    print(min_cnt)


