import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
S = int(input())
stores = [list(map(int, input().split())) for _ in range(S)]
print(stores)
# 4321 = 동서남북