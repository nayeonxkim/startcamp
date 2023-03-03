import sys
sys.stdin = open('input.txt')

def line(arr):
    for i in range(N):
        point = 0
        for j in range(N):
            if arr[i][j] == 'o':
                point += 1
                if point == 5:
                    return 1
            else:
                point = 0
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 가로세로
    ans1 = line(arr)
    arr_t = list(zip(*arr))
    ans2 = line(arr_t)

    # 좌 -> 우 대각선
    point = 0
    ans3 = 0
    for i in range(N):
        for j in range(N):
            row, col = i, j
            while arr[row][col] == 'o':
                point += 1
                row += 1
                col += 1
                if point == 5:
                    ans3 = 1
                    break
                if row >= N or col >= N:
                    break
            point = 0

    # 우 -> 좌 대각선
    point = 0
    ans4 = 0
    for i in range(N):
        for j in range(N):
            row, col = i, j
            while arr[row][col] == 'o':
                point += 1
                row += 1
                col -= 1
                if point == 5:
                    ans4 = 1
                    break
                if row >= N or col < 0:
                    break
            point = 0

    if ans1 or ans2 or ans3 or ans4:
        ans = 'YES'
    else:
        ans = 'NO'

    print(f'#{tc} {ans}')