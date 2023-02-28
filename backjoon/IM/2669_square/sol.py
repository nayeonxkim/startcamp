import sys
sys.stdin = open('input.txt')

# 최대값 100을 이용하여 미리 배열을 생성해둔다.
arr = [[0] * (101) for _ in range(101)]

# 입력값 4개를 리스트로 묶어 리스트 안에 저장 : 2차원 리스트
point = [list(map(int, input().split())) for _ in range(4)]

# 2차원 리스트에서 1차원 리스트 하나씩 꺼낸다.
for p in point:
    # 0번, 2번 인덱스가 행
    for i in range(p[0], p[2]):
        # 1번, 3번 인덱스가 열
        for j in range(p[1], p[3]):
            # 네모 색칠하기 ~
            # 겹치는거 알 필요없으니까 그냥 죄다 1로 넣는다.
            arr[i][j] = 1

# 1의 개수를 센다.
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            cnt += 1
print(cnt)