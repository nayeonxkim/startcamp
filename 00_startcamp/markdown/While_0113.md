# While 문

6개 숫자 랜덤으로 뽑기

```python
ans = []
while True:
    ans.append(rd.choice(numbers))
    if len(ans) == 6:
        break
print(ans)
```

- 리스트 만들어서 숫자 하나씩 추가하기

- 리스트로 출력 가능

- 무한반복 while문 + if 종료조건

```python
cnt = 0
while cnt<6:
    print(rd.choice(numbers))
    cnt+=1
```

- cnt가 하나씩 추가되면서 조건에 해당하면 반복문 멈춤

- 이게 더 깔끔 

- 조건있는 while문

-  <mark>같은 값이 여러 번 출력되는 문제</mark>

```python
ans = []
while x<6:
    a = rd.choice(numbers)
    ans.append(a)
    numbers.remove(a)
    x+=1
print(ans)
```
