import sys
sys.stdin = open('input.txt')

# (1,3)
def boy(num):
    for i in range(1, N+1):
        if not i % num:
            if switch[(i-1)] == 1:
                switch[(i-1)] = 0
            else:
                switch[(i-1)] = 1

def girl(num):
    idx = num - 1
    if switch[idx] == 1:
        switch[idx] = 0
    else:
        switch[idx] = 1

    i = 1
    while idx-i >= 0 and idx+i < N:
        if switch[idx-i] == 0 and switch[idx+i] == 0:
            switch[idx-i] = switch[idx+i] = 1
        elif switch[idx-i] == 1 and switch[idx+i] == 1:
            switch[idx - i] = switch[idx + i] = 0
        i += 1


N = int(input())
switch = list(map(int, input().split()))

M = int(input())
students = [[] * M for _ in range(M)]
for i in range(M):
    students[i] = tuple(map(int, input().split()))


for tp in students:
    num = tp[1]
    if tp[0] == 1:      # 남학생이면
        boy(num)
    else:
        girl(num)

if N > 20:
    for i in range(N):
        if not i % 20:
            for n in range(21):
                if i+n < N:
                    print(switch[i+n], end = ' ')
            print()

else:
    print(*switch)