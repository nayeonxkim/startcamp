import sys
sys.stdin = open('input.txt')

# 남학생
def boy(num):
    # 숫자 1부터 N+1까지 : 1~8까지
    for i in range(1, N+1):
    # 만약 해당 숫자가 주어진 값의 배수라면, : 1~8 중 3의 배수인 숫자의 경우
        if i % num == 0:
            # 해당 순서의 스위치를 바꿔준다. : 인덱스 = 숫자 - 1
            if switch[i-1] == 1:
                switch[i-1] = 0
            else:
                switch[i-1] = 1

# 여학생
def girl(num):
    # 인덱스 = 주어진 숫자 - 1
    idx = num - 1
    # 해당 인덱스의 값을 바꾼다.
    if switch[idx] == 1:
        switch[idx] = 0
    else:
        switch[idx] = 1

    # idx를 기준으로 양 옆을 비교하며 두 개가 같으면 둘 다 값을 바꿔준다.
    # i를 1부터 하나씩 증가시키며 한 칸씩 이동하며 대칭을 확인한다.
    i = 1
    # 스위치 배열을 벗어나지 않을때까지 계속 대칭인지 확인한다.
    while idx-i >= 0 and idx+i < N:
        if switch[idx-i] == 0 and switch[idx+i] == 0:
            switch[idx-i] = switch[idx+i] = 1
        elif switch[idx-i] == 1 and switch[idx+i] == 1:
            switch[idx - i] = switch[idx + i] = 0

        # 만약 두 값이 다른 경우 while문을 종료해주어야한다.
        # 종료하지 않으면 두 값이 달라도 i를 증가시켜 그 다음 값들이 대칭인지 확인하기 때문에
        # 0 1 1 0 1 0 0 같은 경우, 2번 6번 인덱스가 다르기 때문에 대칭이 깨졌음에도
        # 그 다음 1번 7번을 비교하여 두 값을 바꿔버린다.
        else:
            break
        i += 1


# 스위치의 개수와 스위치 기존 상태 입력받음.
N = int(input())
switch = list(map(int, input().split()))

# 스위치를 바꾸는 횟수와 스위치를 바꾸는 조건(성별, 기준 숫자)을 입력받음.
M = int(input())
students = [[] * M for _ in range(M)]
for i in range(M):
    students[i] = tuple(map(int, input().split()))

# 스위치를 바꾸는 조건을 튜플로 입력받아 리스트로 저장하였기 때문에
# 리스트를 순회하며 튜플의 0번이 1이면 남학생 함수를, 2면 여학생 함수를 실행시킨다.
for tp in students:
    num = tp[1]
    if tp[0] == 1:      # 남학생이면
        boy(num)
    else:
        girl(num)

# 20개씩 줄을 바꿔가며 출력해야함
if N > 20:
    for i in range(N):
        if not i % 20:
            print(*switch[i:i+20])
else:
    print(*switch)