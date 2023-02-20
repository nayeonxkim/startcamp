
# 4방향 탐색
# 각 인덱스 = 숫자가 의미하는 이동방향
# 예) 0의 경우, 오른쪽으로 이동 -> di, dj의 0번 = 오른쪽
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 입력값을 받습니다.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr와 같은 모양의 visited 배열을 생성합니다.
    visited = [[0] * N for _ in range(N)]
    # 왼쪽 맨 윗 칸에서 출발하므로 visited[0][0]에 방문기록을 남깁니다.
    visited[0][0] = 1

    # 마찬가지로, 출발지점을 스택에 넣고 시작합니다.
    stack = [(0, 0)]
    # 이동방향을 넣어줄 리스트를 생성합니다.
    energy_lst = []
    # 스택에 값이 존재하는 동안 반복합니다.
    while stack:
        # 스택의 top을 현재 위치로 설정합니다.
        row, col = stack.pop()
        # 이동방향 리스트에 현재 위치의 값을 넣어줍니다.
        energy_lst.append(arr[row][col])

        # 현재 위치의 값과 일치하는 di, dj의 인덱스에 따라 이동합니다.
        ni = row + di[arr[row][col]]
        nj = col + dj[arr[row][col]]

        # 만약 방문기록이 없다면, stack에 해당 좌표를 push하고 방문기록을 남깁니다.
        if not visited[ni][nj]:
            stack.append((ni, nj))
            visited[ni][nj] = 1

    # 중복된 방향을 제거하기 위한 스택을 생성합니다.
    energy_stack = []
    # 에너지 리스트를 순회하며
    for n in energy_lst:
        # 스택에 값이 없거나, 해당 방향이 stack의 top과 다르다면
        # 해당 방향을 stack에 push합니다.
        if not energy_stack or energy_stack[-1] != n:
            energy_stack.append(n)

    print(f'#{tc}', *energy_stack)
