```python
T = int(input())
for i in range(1, T + 1):
    t_num=int(input())
    score=list(map(int,input().split()))
    cnt={}   
    for j in score:
        cnt[j]=score.count(j)
        max_key=max(cnt,key=cnt.get)
    print(f'#{i} {max_key}')
```

- Python언어
- 62,796 kb메모리
- 691 ms실행시간
- 236코드길이

{95: 3, 23: 0, 48: 1}

- value가 가장 큰 key 출력

---

```python
T = int(input())
for i in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * 101
    for j in range(len(lst)):
        num[lst[j]] += 1
    mx = 0
    ans = 0
    for j in range(len(num)):
        if mx <= num[j]:
            mx = num[j]
            ans = j
    print(f'#{n} {ans}')
```

- Python언어
- 50,472 kb메모리
- 102 ms실행시간
- 2,085코드길이

[1, 0, 4, 5]

- 가장 큰 값의 index 출력

- mx를 큰 값으로 업데이트

- ans에 인덱스 저장

---

```python
T = int(input())
for i in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * 101
    mx = 0
    ㅑ= 0
    for j in range(len(num)):
        if mx <= num[j]:
            mx = num[j]
            ans = j
    print(f'#{n} {ans}')
```

[1, 0, 4, 5]

- 가장 큰 값의 index 출력

- mx의 인덱스를 출력

- ans에 인덱스 저장
