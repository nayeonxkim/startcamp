def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    max = 0                 # max값을 계속해서 업데이트하기 위해 처음에는 0을 할당해줍니다.    
    for s in scores:        # scores리스트의 모든 요소를 순회합니다.
        if s >= max:        # scores의 요소s가 기존의 max보다 크거나 같은 경우,
            max = s         # max의 값을 s로 업데이트(재할당)합니다.
    return max              # max값을 반환합니다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
