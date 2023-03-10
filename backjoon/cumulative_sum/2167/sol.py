import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        res[i+1][j+1] =arr[i][j] + res[i+1][j] + res[i][j+1] - res[i][j]

K = int(sys.stdin.readline())
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    ans = res[x2][y2] -res[x2][y1-1] - res[x1-1][y2] + res[x1-1][y1-1]
    print(ans)