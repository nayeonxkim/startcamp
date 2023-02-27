import sys
sys.stdin = open('month_input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 총 비용, 심은 나무의 수, 심은 나무 중 가장 비싼 나무의 가격
    total_cost = cnt = max_cost = 0

    # 모든 행에 대하여
    for i in range(N):
        # 짝수 열에 대하여 (가장 왼쪽부터 한 줄씩 띄어서 )
        for j in range(0, M, 2):

            # 총 비용에 각 나무의 비용을 더한다.
            total_cost += arr[i][j]

            # 심은 나무의 수에 1을 추가한다.
            cnt += 1

            # 현재 가장 비싼 나무의 가격보다 나무의 가격이 더 비싸다면
            if max_cost <= arr[i][j]:
                # max_cost를 업데이트하고
                max_cost = arr[i][j]

                # 해당 나무의 열 번호를 max_col로 정한다.
                max_col = j

    # 문제에서는 0번 인덱스를 1번 열로 표현하기 때문에 구해진 max_col에 1을 더해준다.
    print(f'#{tc} {total_cost} {cnt} {max_cost} {max_col+1}')