import sys
sys.stdin = open('month_input2.txt')

T = int(input())
for tc in range(1, T+1):
    N, K, A, B = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]


    # 기존 배열에서  총 별의 개수를 센다.
    original_star = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                original_star += 1


    # 촬영영역에 해당하는 만큼만 새로운 배열로 생성
    new_arr = []
    for i in range(A - K//2, A + K//2 + 1):
        new_lst = []
        for j in range(B - K//2, B + K//2 + 1):
            # 기존 배열을 벗어나지 않는 범위만 촬영영역으로 설정한다.
            if 0 <= i < N and 0 <= j < N:
                new_lst.append(arr[i][j])
        new_arr.append(new_lst)


        # ans = 별을 찍을 수 있는 확대 횟수
        # 확대하지 않은 첫 촬영영역부터 촬영이 불가능한 경우, 실패를 반환해야하므로 초기값을 -1로 설정한다.
        # p = 확대하는 크기
        ans = -1
        p = 0

        while True:

            star = 0

            # 처음엔 확대하지 않고 확인 -> 위아래 양옆을 한 칸씩만 확대 -> 다음번엔 2칸씩 확대 : p를 1씩 늘리며 계속 반복
            for i in range(p, len(new_arr) - p):
                for j in range(p, len(new_lst) - p):
                    # 확대한 영역에서 *의 갯수를 센다.
                    if new_arr[i][j] == '*':
                        star += 1

            # 확대한 영역의 별의 갯수가 기존의 별의 갯수와 같다면 ans를 1 증가시킨다.
            if star == original_star:
                ans += 1

            # 촬영할 수 있는 별의 개수가 기존과 달라진다면 더 이상 확대하는 것이 의미없으므로 반복문을 종료시킨다.
            else:
                break

            # 반복문이 종료되지 않았다면, p를 1증가시킨다.
            p += 1

    print(f'#{tc} {ans}')




