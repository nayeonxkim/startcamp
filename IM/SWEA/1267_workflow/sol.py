import sys
sys.stdin = open('input.txt')

for tc in range(1, 4):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    arr = [[0] * (V+1) for _ in range(V+1)]
    print(edge, E)
    for n in range(E):
        i, j = edge[n*2], edge[n*2+1]
        arr[i][j] = 1
    for i in range(V+1):
        print(arr[i])

    start = []
    for j in range(1, V+1):
        sum_col = 0
        for i in range(1, V+1):
            sum_col += arr[i][j]
        if sum_col == 0:
            start.append(j)
    print(start)