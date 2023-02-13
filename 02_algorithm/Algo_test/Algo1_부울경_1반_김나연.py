T = int(input())
# 테스트 케이스 횟수만큼 모든 과정을 반복합니다.
for tc in range(1, T+1):
    # N과 M을 입력받아 변수에 할당합니다.
    N, M = map(int, input().split())

    # N*N의 0배열을 생성합니다.
    arr = [[0] * N for _ in range(N)]

    # 도장을 찍은 횟수만큼 왼쪽 모서리 좌표와 너비, 넓이를 입력받고
    for _ in range(M):
        row, col, width, height = map(int, input().split())
        # 배열에서 도장의 크기만큼, 해당하는 위치에 1을 할당합니다.
        for i in range(row, row+height):
            for j in range(col, col+width):
                arr[i][j] = 1

   # 배열에서 1의 개수를 세어 출력합니다.
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt += 1
    print(f'#{tc} {cnt}')