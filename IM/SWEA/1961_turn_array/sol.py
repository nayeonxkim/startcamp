import sys
sys.stdin = open('input.txt')

# 열우선 조회 : 0 -> 1 -> 2 열 순으로 탐색
# 행을 반대로 조회 : 2 -> 1 -> 0 행 순으로 탐색
def turn(arr):
    new_arr = []
    for j in range(N):
        new_str = ''
        for i in range(N-1, -1, -1):
            new_str += str(arr[i][j])
        new_arr.append(new_str)

    return new_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = turn(arr)
    arr_180 = turn(arr_90)
    arr_270 = turn(arr_180)

    print(f'#{tc}')
    for i in range(N):
        print(arr_90[i], arr_180[i], arr_270[i])
