import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input()))
    print(arr[i])

visited = [[0] * N for _ in range(N)]
total_cnt = []
cnt = 1
# 델타 : 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
print(visited.count(1))
print(arr.count(1))
while arr.count(1):
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not visited[i][j]:
                row, col = i, j
                break


    # 시작지점 방문기록
    stack = [(row, col)]
    print(stack)
    visited[row][col] = 1



    while stack:
        row, col = stack.pop()
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))
                    cnt += 1


