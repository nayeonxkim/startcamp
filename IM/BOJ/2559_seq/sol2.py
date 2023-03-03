import sys
sys.stdin = open('input.txt')

# 10 5
# 3 -2 -4 -9 0 3 7 13 8 -3
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 더해주는 수만큼만 sum 배열을 생성한다.
# arr랑 같은 길이로 만들면 수열의 모든 수가 음수인 경우 : -100 -100 2개씩 합
# sum = [0, -200, 0] 이 되어 최대 값을 0으로 반환한다.
# 따라서 sum = [0, -200]으로 생성하도록 전체 길이를 설정해주고,
# sum[1:]의 최대값을 반환한다.
sum = [0] * (N-K+2)

# 첫 항 만들기
# S1 = A0~A4의 합 : arr의 0번부터 K개의 합
for k in range(K):
    sum[1] += arr[k]

# 누적합 수열 만들기
# S2 = S1 + A5 - A0
# S3 = S2 + A6 - A1
for i in range(2, len(sum)):
    sum[i] = sum[i-1] + arr[i-2+K] - arr[i-2]
print(max(sum[1:]))