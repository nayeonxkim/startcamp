import sys
sys.stdin = open('input.txt')

# 단조 확인 함수
# 숫자를 문자열로 바꾸어 앞 글자가 뒷 글자비교
# 길이가 1이면 단조 확인할 필요없이 바로 1 반환
# 뒷 글자가 크면 0을 반환하여 max_num은 초기값인 -1 그대로.
# 앞 글자가 크면 point + 1, point가 숫자의 길이만큼 커지면 해당 숫자는 모든 자릿수에 대해 조건에 일치
# -> 1 반환하여 if문 돌아가서 max_num 업데이트
def danzo(num):
    number = str(num)
    point = 1
    if len(number) == 1:
        return 1
    else:
        for i in range(len(number)-1):
            if number[i] > number[i+1]:
                return 0
            else:
                point += 1
                if point == len(number):
                    return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = -1
    # 2 3 4 7
    # 반복문 돌면서 숫자 만듦
    # 곱할 기준 숫자 : 마지막 숫자는 기준 숫자로 잡지 않아도 되므로 N-1까지 (2)
    for n in range(N-1):
        # 기준 숫자 다음 수부터 끝까지 (3 4 7)
        for i in range(n+1, N):
            # 기준 숫자 * 다른 수 (2*3, 2*4, 2*7)
            num = numbers[n] * numbers[i]

            # 만들어진 숫자가 단조라면 최대값과 비교하여 업데이트
            if danzo(num):
                if max_num < num:
                    max_num = num

    print(f'#{tc} {max_num}')
