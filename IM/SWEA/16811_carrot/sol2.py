import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    # 당근의 크기 1~30
    size = [0] * 31
    for c in carrot:
        size[c] += 1

    minV = 1000
    # 1부터 28까지 소박스
    for i in range(1, 29):
        # 소박스에 넣은 당근 다음 값부터 29까지 중박스
        for j in range(i+1, 30):
            # 1부터 i까지의 합 = 소박스에 들어갈 당근 갯수
            A = sum(size[1:i+1])
            # i+1부터 j까지의 합 = 중박스 당근 갯수
            B = sum(size[i+1:j+1])
            # j+1부터 30까지의 합 = 대박스 당근 갯수
            C = sum(size[j+1:31])
            if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                V = max  (A, B, C) - min(A, B, C)
                if minV > V:
                    minV = V
    if minV == 1000:
        minV = -1

    print(f'#{tc} {minV}')