import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# K = 2
# k = 0, 1
max_ans = -1000000
for i in range(N-K+1):
    ans = 0
    for k in range(K):
        ans += arr[i+k]
    if max_ans < ans:
        max_ans = ans
print(max_ans)