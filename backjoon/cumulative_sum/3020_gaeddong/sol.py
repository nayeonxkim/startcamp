import sys
sys.stdin = open('input.txt')

N, H = map(int, sys.stdin.readline().split())

upper = [0] * (N//2)
lower = [0] * (N//2)

for i in range(N//2):
    lower[i] = int(sys.stdin.readline())
    upper[i] = int(sys.stdin.readline())

print(lower, upper)