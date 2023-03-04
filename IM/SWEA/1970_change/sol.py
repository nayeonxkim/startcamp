import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    change = [0] * 8

    while N >= 50000:
        N -= 50000
        change[0] += 1
    while N >= 10000:
        N -= 10000
        change[1] += 1
    while N >= 5000:
        N -= 5000
        change[2] += 1
    while N >= 1000:
        N -= 1000
        change[3] += 1
    while N >= 500:
        N -= 500
        change[4] += 1
    while N >= 100:
        N -= 100
        change[5] += 1
    while N >= 50:
        N -= 50
        change[6] += 1
    while N >= 10:
        N -= 10
        change[7] += 1
    print(f'#{tc}')
    print(*change)