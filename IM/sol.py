import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                stack = [(i, j)]


    cnt = 0
    for i in range(3):
        stack1 = []
        while stack:

            row, col = stack.pop()

            for i in range(row-1, 0, -1):
                if arr[i][col] == 1:
                    n = 1
                    while i - n >= 0:
                        if arr[i-n][col] == 1 and visited[i-n][col] == 0:
                            cnt += 1
                            visited[i-n][col] = 1
                            stack1.append((i - n, col))
                            break
                        else:
                            stack1.append((i - n, col))
                            visited[i - n][col] = 1
                            n += 1
                    break

            for i in range(row+1, N-1):
                if arr[i][col] == 1:
                    n = 1
                    while i + n < N:
                        if arr[i+n][col] == 1 and visited[i+n][col] == 0:
                            cnt += 1
                            visited[i + n][col] = 1
                            stack1.append((i + n, col))
                            break
                        else:
                            stack1.append((i+n, col))
                            visited[i + n][col] = 1
                            n += 1

                    break

            for j in range(col-1, 0, -1):
                if arr[row][j] == 1:
                    n = 1
                    while j - n >= 0:
                        if arr[row][j - n] == 1 and visited[row][j-n] == 0:
                            cnt += 1
                            visited[row][j-n] = 1
                            stack1.append((row, j - n))
                            break
                        else:
                            stack1.append((row, j - n))
                            visited[row][j - n] = 1
                            n += 1

                    break

            for j in range(col+1, N-1):
                if arr[row][j] == 1:
                    n = 1
                    while j+n < N:
                        if arr[row][j+n] == 1 and visited[row][j+n] == 0:
                            cnt += 1
                            visited[row][j + n] = 1
                            stack1.append((row, j + n))
                            break
                        else:
                            stack1.append((row, j+n))
                            visited[row][j + n] = 1
                            n += 1

                    break

        stack = stack1[:]

    print(f'#{tc} {cnt}')