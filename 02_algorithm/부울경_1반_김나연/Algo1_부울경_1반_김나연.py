
# 8방향 탐색
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

# 입력값을 받습니다.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 봉우리 값을 넣어줄 리스트를 생성합니다.
    top_lst = []

    # 모서리를 뺀 구역을 대상으로 8방향을 탐색합니다.
    for i in range(1, N-1):
        for j in range(1, N-1):
            # 해당 구역보다 더 낮은 구역의 개수를 세기위한 변수를 생성합니다.
            cnt = 0
            # 8방향을 탐색하며 해당 구역보다 값이 작으면 cnt에 1을 더해줍니다.
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if arr[ni][nj] < arr[i][j]:
                    cnt += 1
            # 주변 8지역 모두 중심지역보다 값이 작으면 cnt가 8이 됩니다.
            # 따라서 cnt가 8인 경우, top_lst에 해당 중심지역의 값을 추가합니다.
            if cnt == 8:
                top_lst.append(arr[i][j])

    # 봉우리가 하나만 있거나 없는 경우, -1을 반환합니다.
    if len(top_lst) <= 1:
        ans = -1
    # 그 외의 경우에는 가장 높은 봉우리와 가장 낮은 봉우리의 차를 반환합니다.
    else:
        ans = max(top_lst) - min(top_lst)

    print(f'#{tc} {ans}')