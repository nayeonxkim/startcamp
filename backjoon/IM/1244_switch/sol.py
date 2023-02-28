import sys
sys.stdin = open('input.txt')

# (1,3)
def boy(num):
    pass



N = int(input())
switch = list(map(int, input().split()))

M = int(input())
students = [[] * M for _ in range(M)]
for i in range(M):
    students[i] = tuple(map(int, input().split()))

print(students)

for tp in students:
    num = tp[1]
    if tp[0] == 1:      # 남학생이면
        boy()