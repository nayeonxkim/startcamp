import sys
sys.stdin = open('input.txt')


di = [0, 1, 1, 1, ]
dj = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]



    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(3):
                ni = i + di[k]
                nj = j + dj[k]
