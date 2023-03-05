import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
data = [list(map(int, input().split())) for _ in range(5)]

ans = []
for lst in data:
    for n in lst:
        ans.append(n)

def check_bingo(arr):
    bingo = 0

    for lst in arr:
        if all(n == 0 for n in lst):
            bingo += 1
            if bingo == 3:
                return bingo

    arr_t = list(zip(*arr))
    for lst in arr_t:
        if all(n == 0 for n in lst):
            bingo += 1
            if bingo == 3:
                return bingo

    point = 0
    for i in range(5):
        if arr[i][i] == 0:
            point += 1
            if point == 5:
                bingo += 1
                if bingo == 3:
                    return bingo
        else:
            break

    point = 0
    for i in range(5):
        if arr[i][4 - i] == 0:
            point += 1
            if point == 5:
                bingo += 1
        else:
            break

    return bingo

def make_res():
    # 5를 부른 상황
    for n in ans:
        for i in range(5):
            for j in range(5):
                # arr를 돌면서 n과 같은 값을 찾고,
                if arr[i][j] == n:
                    # 같다면 0으로 바꾸고 빙고 검사
                    arr[i][j] = 0
                    if check_bingo(arr) == 3:
                        return ans.index(n) + 1


print(make_res())
