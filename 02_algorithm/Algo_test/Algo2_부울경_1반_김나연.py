T = int(input())
# 테스트 케이스 횟수만큼 반복합니다.
for tc in range(1, T+1):
    N = int(input())

    # 망치의 위치를 입력받아 변수에 할당합니다.
    r, c = map(int, input().split())


    for _ in range(N):
        ## 10*10 게임판을 생성합니다.
        # 망치가 두더지로 가는 길을 1로 표시하기 위해
        # 새로운 두더지가 올라올 때마다 게임판을 새로 생성합니다.
        arr = [[0] * 10 for _ in range(10)]

        # 두더지의 좌표와 두더지가 머무르는 시간을 입력받아 변수에 할당합니다.
        target_r, target_c, K = map(int, input().split())

        ## 망치와 두더지 사이의 길을 1로 나타냅니다.
        # 망치와 두더지 사이에 꺾이는 길의 좌표를 구합니다.
        # 둘 중 더 큰 row값이 turn_r가 되고, 더 작은 row의 col값이 turn_c가 됩니다.
        rows = [r, target_r]
        cols = [c, target_c]

        turn_r = max(target_r, r)
        turn_c = cols[rows.index(min(target_r, r))]


        # row와 col을 각각 두더지와 망치의 위치중 더 작은 값에서 더 큰 값까지
        # turn좌표를 기준으로, 일직선으로 1을 할당합니다.
        for i in range(min(r, target_r), max(r,target_r)+1):
            arr[i][turn_c] = 1

        for j in range(min(c, target_c), max(c,target_c)+1):
            arr[turn_r][j] = 1

        # 두더지가 있는 곳에 2를 할당합니다.
        arr[target_r][target_c] = 2

        # 현재 위치에서 출발하여 K번 안에 두더지가 있는 위치까지 도착하면 point에 1을 추가합니다.
        # 가로로 먼저 이동하도록 설정합니다.
        point = 0
        while K != 0:
            if arr[r][c+1] != 0:
                arr[r][c] = 0
                c += 1

            elif arr[r][c-1] != 0:
                arr[r][c] = 0
                c -= 1

            elif arr[r+1][c] != 0:
                arr[r][c] = 0
                r += 1

            elif arr[r-1][c] != 0:
                arr[r][c] = 0
                r -= 1

            if arr[r][c] == 2:
                point += 1
                break
            K -= 1

    print(f'#{tc} {point}')
