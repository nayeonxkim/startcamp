import sys
sys.stdin = open('input.txt')

N1 = int(input())
# N_lst에 두번째에 올 수 있는 모든 수를 집어넣는다.
# N1보다 작거나 **같은**수가 올 수 있다.
N_lst = [n for n in range(N1 + 1)]


max_len = 0
max_numbers = []

# N2 후보군을 모두 순회하며 이어진 수의 리스트를 생성하고,
# 조건에 부합하는 (0이상) 숫자들만 리스트에 추가하여 리스트를 완성한다.
for N2 in N_lst:
    numbers = [N1, N2]

    for i in range(30001):
        N = numbers[i] - numbers[i+1]
        if N >= 0:
            numbers.append(N)
        else:
            break

    # 만들어진 수의 리스트가 현재 최고 길이보다 길다면,
    # 해당 리스트를 max_lst로 한다.
    if max_len < len(numbers):
        max_len = len(numbers)
        max_lst = numbers

print(max_len)
print(*max_lst)