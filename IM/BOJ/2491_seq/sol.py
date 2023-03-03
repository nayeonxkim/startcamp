import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))

max_cnt = 0
for n in range(N-1):
    cnt1 = 1
    for i in range(n, N-1):
        if lst[i] > lst[i+1]:
            break
        if max_cnt > N - 1 - i:
            break
        else:
            cnt1 += 1

    if max_cnt < cnt1:
        max_cnt = cnt1

for n in range(N-1):
    cnt2 = 1
    for i in range(n, N-1):
        if lst[i] < lst[i+1]:
            break
        if max_cnt > N - 1 - i:
            break
        else:
            cnt2 += 1
    if max_cnt < cnt2:
        max_cnt = cnt2

print(max_cnt)