import sys
sys.stdin = open('input.txt')

### 기둥정보를 담은 1차원 배열 완성하기 ###
N = int(input())
arr = [0] * 1001
# 기둥 정보 입력받음.
# 각 기둥의 왼쪽 면 = 배열의 인덱스, 높이 = 배열의 값
max_idx = 0
for _ in range(N):
    i, arr[i] = map(int, input().split())

    # 인덱스가 가장 큰 값을 구한다.
    if max_idx < i:
        max_idx = i

# 가장 큰 인덱스 이후로는 값이 죄다 0이므로 그 뒤는 버린다.
arr = arr[:max_idx+1]

### 창고의 넓이 구하기 ###
max_val = 0
max_i = 0
# 가장 높은 기둥을 기준으로 왼쪽, 오른쪽 나누어야함.
for i in range(len(arr)):
    if max_val < arr[i]:
        max_val = arr[i]
        max_i = i

# 가장 높은 기둥의 왼쪽 = front, 오른쪽 = back
front = arr[:max_i+1]
back = arr[max_i:]


# 자신보다 낮거나 같은 값은 자신으로 바꾸어준다.
# 4 0 3 3 6 0 3 -> 4 4 4 4 6 6 6
def roof(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            lst[i + 1] = lst[i]
    return lst

# back의 경우 가장 높은 값이 0번에 있으므로 reverse해준다.
roof(front)
back.reverse()
roof(back)

# front, back 배열의 값들을 모두 더하여 창고의 면적을 구한다.
ans = 0
for i in range(len(front)):
    ans += front[i]
for j in range(len(back)-1):
    ans += back[j]

print(ans)