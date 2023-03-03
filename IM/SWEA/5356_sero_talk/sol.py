import sys
sys.stdin = open('input.txt')

# 문자열의 최대 길이를 구하여 그보다 짧은 문자열에는 ''을 더해주어 가로 길이를 맞춘다.
# 문자열 중간에 빈칸이 오지 않으므로 가능한 풀이

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    # 행별로 조사하여 가장 긴 길이를 구한다.
    max_len = 0
    for lst in arr:
        if max_len < len(lst):
            max_len = len(lst)

    # 길이가 최대 길이보다 짧은 행에는 공백을 그 길이만큼 더해주어
    # 모든 행의 길이를 최대 길이로 맞추어준다.
    for lst in arr:
        if max_len > len(lst):
            lst += [''] * (max_len - len(lst))

    # 열 우선순회하여 문자열을 세로로 읽는다.
    ans = ''
    for j in range(max_len):
        for i in range(5):
            ans += arr[i][j]
    print(f'#{tc} {ans}')
