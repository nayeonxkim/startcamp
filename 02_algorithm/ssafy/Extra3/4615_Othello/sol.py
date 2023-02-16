import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]

    i = N//2
    arr[i][i] = arr[i-1][i-1] = 2
    arr[i][i-1] = arr[i-1][i] = 1

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]


    for _ in range(M):
        i, j, color = map(int, input().split())
        row = i - 1
        col = j - 1

        arr[row][col] = color

        for k in range(8):
            ni = row + di[k] * 2
            nj = col + dj[k] * 2
            mi = row + di[k]
            mj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == color:
                    if arr[mi][mj] and arr[mi][mj] != color:
                        arr[ni][nj] = color

        for i in range(N):
            print(arr[i])
        print()

        # if ni > row:
        #     r = ni - 1
        # elif ni < row:
        #     r = ni + 1
        # else:
        #     r = ni
        #
        # if nj > col:
        #     c = nj - 1
        # elif nj < col:
        #     c = nj + 1
        # else:
        #     c = nj
        #
        # arr[r][c] = color


    # for i in range(N):
    #     print(arr[i])
