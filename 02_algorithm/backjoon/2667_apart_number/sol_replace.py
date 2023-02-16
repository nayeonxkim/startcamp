import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input()))
    print(arr[i])

visited = [[0] * N for _ in range(N)]
stack = []

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
cnt = 0

while True:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                stack.append((i, j))
                visited[i][j] = 1
                cnt += 1
                break

    cnt_per = 0
    while stack:
        row, col = stack.pop()

        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt_per += 1
            print(cnt_per)