import random as rd

# range()는 range자체만 생성, 리스트로 만들려면 list()사용하여 따로 지정해주어야함.
numbers = list(range(1,46))
print(numbers)

#리스트 값에서 무작위로 뽑기
## for문
for i in range(6):
    print(rd.choice(numbers))

## while문
ans = []
while True:
    ans.append(rd.choice(numbers))
    if len(ans) == 6:
        break
print(ans)

## while문
cnt = 0
while cnt<6:
    print(rd.choice(numbers))
    cnt+=1

# 중복되는 숫자 없도록 하기
ans = []
x=0
while x < 6:
    a = rd.choice(numbers)
    ans.append(a)
    numbers.remove(a)
    x+=1
print(ans)

# random 모듈의 sample 사용하기
print(rd.sample(numbers,6))


# 위 가정 다섯번 반복하는 함수 정의하기
for i in range(5):
    print(rd.sample(numbers,6))