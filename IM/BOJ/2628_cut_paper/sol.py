import sys
sys.stdin = open('input.txt')

# 가로길이, 세로길이
N, M = map(int, input().split())

# 각 길이 만큼 배열 생성 및 복사
# 가로 길이 10 -> 0~9 배열 생성
H = list(range(N))
H_lst = H[:]
W = list(range(M))
W_lst = W[:]

# 자르기 조건 입력 받기
# 가로로 자르는 조건, 세로로 자르는 조건을 각각 배열에 저장함
# 가로로 3번 점선 자르기 -> width에 값 3 추가
width = []
height = []
L = int(input())
for _ in range(L):
    a, num = map(int, input().split())
    if a:
        height.append(num)
    else:
        width.append(num)

# 자르기 조건 배열 정렬
width.sort()
height.sort()

# 가로세로 길이 배열에서,
# 자르기 조건 숫자보다 작은 값의 개수를 세어 ans1 배열에 저장한다.
# 가로길이 배열 : [0, 1, 2, ..., 7]
# 자르기 조건 숫자 : 2
# 길이배열에서 조건 수보다 작은 수 0, 1
# -> ans1에 2 저장
# -> 가로길이 배열에서 1다음 수 2부터 조사한다.

# 가로
ans1 = []
for n in width:
    cnt = 0
    for m in W_lst:
        if m < n:
            cnt += 1
            W_lst = W[m+1:]
    ans1.append(cnt)
# 전체 가로 길이에서 잘려나간 조각의 길이합을 빼주어 나머지 조각의 길이를 구한다.
ans1.append(M - sum(ans1))

# 세로
ans2 = []
for n in height:
    cnt = 0
    for m in H_lst:
        if m < n:
            cnt += 1
            H_lst = H[m+1:]
    ans2.append(cnt)
ans2.append(N - sum(ans2))

# ans1, ans2에는 가로세로별로 잘려진 조각의 길이들이 저장된다.
# 가장 긴 조각들을 곱하여 가장 큰 종이조각의 넓이를 구한다.
ans = max(ans1) * max(ans2)
print(ans)