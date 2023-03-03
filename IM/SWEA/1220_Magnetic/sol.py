import sys
sys.stdin = open('input.txt')

# 내가 1인 경우, 빨간 색인 경우 s로 향한다. : 행 번호가 1씩 증가하며 99까지 가서 사라짐
def to_s(i, j):
    while arr[i+1][j] == 0:
        arr[i][j] = 0
        i += 1
        arr[i][j] = 1
        if i == 99:
            break

# 내가 2인 경우, n으로 향한다. : 행번호가 1씩 감소하며 0까지 간다.
def to_n(i, j):
    while arr[i-1][j] == 0:
        arr[i][j] = 0
        i -= 1
        arr[i][j] = 2
        if i == 0:
            break

for tc in range(1, 11):
    N = int(input()) # 항상 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    ### 자석의 종류에 따라 자석을 이동시킨다. ###
    # 98행부터 올라가며 1번 자석을 99까지 내림
    for i in range(98, -1, -1):
        for j in range(100):
            if arr[i][j] == 1:
                to_s(i, j)

    # 가장 아래 행의 1번 자석 다 없앰
    for j in range(100):
        if arr[99][i] == 1:
            arr[99][1] = 0


    # 1행부터 내려가며 2번 자석을 0번까지 올림
    for i in range(1, 100):
        for j in range(100):
            if arr[i][j] == 2:
                to_n(i, j)

    # 가장 윗 행의 2번 자석 다 없앰
    for j in range(100):
        if arr[0][i] == 2:
            arr[0][1] = 0

    # 결과 -> 이동이 끝난 테이블 반환
    # 이동이 끝난 테이블에서 1,2가 붙어있는 상황을 찾는다.
    ans = 0
    for i in range(99):
        for j in range(100):
            if arr[i][j] == 1 and arr[i+1][j] == 2:
                ans += 1
    print(f'#{tc} {ans}')