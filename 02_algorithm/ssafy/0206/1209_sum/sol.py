import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())

    arr = [list(map(int, input().split())) for i in range(100)]

    # 행의 합
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        sum_lst = [row_sum, col_sum]

    for i in range(100):
        dia_sum = 0
        for j in range(100):
            dia_sum += arr[i][j + (100 - 1 - 2 * j) * (i % 2)]
        sum_lst.append(dia_sum)

    print(max(sum_lst))