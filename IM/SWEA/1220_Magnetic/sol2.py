import sys
sys.stdin = open('input.txt')

# 자석이 N극인 경우 S극 쪽으로 이동시킨다.
def to_s(i, j):
    while True:

        # 2. 99행까지 내려가면 이동을 멈추고 테이블에서 없앤다.
        if i == 99:
            arr[i][j] = 0
            break
        # 3. 99행까지 내려가기전 아래 칸에 다른 자석이 있으면 더이상 이동하지 못한다.
        elif arr[i+1][j] != 0:
            break

        # 1. 자석을 한 칸씩 계속 내린다.
        arr[i][j] = 0
        i += 1
        arr[i][j] = 1

# 자석이 S극인 경우 N극 쪽으로 이동시킨다.
def to_n(i, j):
    while True:

        # 2. 0행까지 올라가면 이동을 멈추고 테이블에서 없앤다.
        if i == 0:
            arr[i][j] = 0
            break

        # 3. 0행까지 올라가기전 위 칸에 다른 자석이 있으면 더이상 이동하지 못한다.
        elif arr[i-1] != 0:
            break

        # 1. 자석을 한 칸씩 계속 올린다.
        arr[i][j] = 0
        i -= 1
        arr[i][j] = 2

for tc in range(1, 11):
    N = int(input()) # 항상 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    ## N극은 아래에 있는 자석부터, S극은 위에 있는 자석부터 처리한다 ##
    # 가장 아래 행에 있는 N극 자석과 가장 윗 행에 있는 S극 자석을 테이블에서 없애준다.
    for i in range(N):
        if arr[99][i] == 1:
            arr[99][i] = 0
        if arr[0][i] == 2:
            arr[0][i] = 0

    # 열 우선 조회
    # 98번 행부터 한 칸씩 올라가며 자석을 이동한다.
    for j in range(N):
        for i in range(N-2, -1, -1):
            if arr[i][j] == 1:
                to_s(i, j)

    # 열 우선 조회
    # 1번 행부터 한 칸씩 내려가며 자석을 이동한다.
    for j in range(N):
        for i in range(1, N):
            if arr[i][j] == 2:
                to_n(i, j)


    # 이동이 끝난 후 교착상태를 확인한다.
    ans = 0
    for i in range(N-1):
        for j in range(N):
            if arr[i][j] == 1 and arr[i+1][j] == 2:
                ans += 1
    print(f'#{tc} {ans}')
