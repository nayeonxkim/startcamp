import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

cnt = 1
max_cnt = 1
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt = 1

cnt = 1
for i in range(N-1):
    if arr[i] >= arr[i+1]:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)