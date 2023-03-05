import sys
sys.stdin = open('input.txt')
K = int(input())
point = [list(map(int, input().split())) for _ in range(6)]

height = []
width = []
for lst in point:
    if lst[0] == 1 or lst[0] == 2:
        width.append(lst[1])
    else:
        height.append(lst[1])

res = max(width) * max(height) - min(width) * min(height)
print(height)
# 면적 X 참외수
ans = res * K
print(ans)