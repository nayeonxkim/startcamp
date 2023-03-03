import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    students = list(range(1, N+1))
    K_lst = list(map(int, input().split()))

    ans = []
    for n in students:
        if n not in K_lst:
            ans.append(n)

    print(f'#{tc}', end = ' ')
    print(*ans)