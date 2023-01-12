```python
A, B = map(int, input().split())
if A-B==2:
  print('B')
elif B-A==2:
  print('A')
elif A>B:
  print('A')
elif A<B:
  print('B')
```

- 44,788 kb메모리
- 97 ms실행시간
- 128코드길이

---

```python
A,B = map(int, input().split())
if A-B==2:
  print('B')
elif B-A==2:
  print('A')
elif A>B:
  print('A')
elif A<B:
  print('B')
```

---

```python
A, B= map(int, input().split())
ans = A-B
if ans==2:
  print('B')
elif ans==-2:
  print('A')
elif ans>0:
  print('A')
elif ans<0:
  print('B')
```

- 58,240 kb메모리
- 141 ms실행시간
- 143코드길이

---

가위 1

바위 2

보 3

이기는 경우

1 > 3

2 > 1

3 > 2

한 명이 이기는 걸로

if 

- 42,216 kb메모리
- 87 ms실행시간
- 121코드길이

---

# 각 자릿수의 합

```python
n=input()
s=0
for i in range(len(n)):
  s+=int(n[i])
print(s)
```

```python
n=int(input())
score=list(map(int,input().split()))
score.sort()
med=int((n-1)/2)
print(score[med])
```
