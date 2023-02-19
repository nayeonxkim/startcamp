import sys
sys.stdin = open('input.txt')

def check_one(arr):

    max_point = 0
    for i in range(len(arr)):
        point = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                point += 1
                if max_point < point:
                    max_point = point
            else:
                point = 0

    return max_point


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 기존 행렬
    ans_row = check_one(arr)

    # 전치 행렬
    arr_t = list(zip(*arr))
    ans_col = check_one(arr_t)

    ans = max(ans_row, ans_col)
    print(f'#{tc} {ans}')