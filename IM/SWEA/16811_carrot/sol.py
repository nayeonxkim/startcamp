import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    # 1. 오름차순 정렬
    carrot.sort()

    # 2. 세 그룹으로 자르기
    minV = 1000
    # 소 박스 : 처음부터 N-3까지
    # (N/2개 조건 생각하지 않고 담을 수 있는 모든 개수 고려)
    for i in range(N-2):
        # 중 박스 : i+1에서 N-2까지
        for j in range(i+1, N-1):
            # 같은 값이 있으면 소/중 박스에 나누어 지면 안됨
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                # 각 박스에 들어가는 당근의 개수
                A = i + 1
                B = j - i
                C = N - 1 - j
                # 모든 박스에 값이 있고, 각 박스마다 당근의 개수가 조건에 맞는 경우
                if A * B * C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    V = max(A, B, C) - min(A, B, C)
                    if minV > V:
                        minV = V

    if minV == 1000:
        minV = -1

    print(f'#{tc} {minV}')