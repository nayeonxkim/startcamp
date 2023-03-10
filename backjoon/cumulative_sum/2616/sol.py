import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# 누적합 구하기 : O(N)
res = [0] * (N+1)
for i in range(N):
    res[i+1] = res[i] + arr[i]
print(res)

# 3개씩의 합 구하기 -> 리스트로 저장 : O(N)
# 한번 끌어진 차는 못끌고가
tot = []
for i in range(N, M, -1):
    print(res[i], res[i-M], '=', res[i] - res[i-M])
    tot.append(res[i] - res[i-M])
# tot.sort(reverse=True)

print(tot)