import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [0] * 1001

for i in range(n):
    l, h  = map(int, input().split())
    arr[l] = h

res = 0
mx = 0
idx = 0
for i in range(1001):
    if mx <= arr[i]:
        res += mx*(i-idx)
        mx = arr[i]
        idx = i

res += mx

mx = 0
idx = 0
for i in range(1000,-1,-1):
    if mx < arr[i]:
        res += mx*(-i+idx)
        mx = arr[i]
        idx = i

print(res)