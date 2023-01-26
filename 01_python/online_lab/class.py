lst = [1, 2, 5, 7, 3, 4, 6]
lst.sort()
print(lst)

scores = [('eng', 88, '강남'), ('math', 93, '도쿄'), ('kor', 85, '나성')]
scores.sort() # 제일 앞에 있는 값(과목명)을 기준으로 정렬함
print(scores)   # 뒤에 있는 값(잠수)을 기준으로 정렬하려면 ?

# sort안에 'key=함수'를 넣으면 해당 값을 기준으로 정렬함
scores.sort(key=lambda x : x[2])