def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    cnt = 0                 # 60점이 넘는 점수들을 count하기 위해 cnt변수를 선언합니다.
    for s in scores:        # scores리스트의 모든 요소를 순회합니다.
        if s >= 60:         # scores의 요소 s가 60이상인 경우,
            cnt += 1        # cnt에 1을 추가합니다.
    return cnt              # cnt를 반환합니다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
