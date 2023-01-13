# 백준

## 반복문

```python
# 1차원 리스트
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(A+B)

# 2차원 리스트
T = int(input())
lst = []
for i in range(T):
    ipt = list(map(int,input().split()))
    lst.append(ipt)

for i in range(len(lst)):
    ans = lst[i][0]+lst[i][1]
    print(ans)
## 메모리 훨씬 많이 쓰임

#  sys 라이브러리
import sys
T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)
## input()보다 훨씬 빠름
```

---

# 3003

```python
inp = list(map(int,input().split()))
base =[1,1,2,2,2,8]
ans=[]
for i in range(len(inp)):
    ans.append(base[i]-inp[i])
for i in range(len(ans)):
    print(ans[i],end=" ")
```

리스트끼리 연산은 +만 된다.

리스트 요소를 리스트 빼고, 공백을 넣어서 출력하기 → for문 사용

---

# 10951

```python
while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break
```

종결규칙이 없는 while 문

아무것도 입력되지 않을 때 종료되게 해야함

`try except` : except는 예외문 설정 예외 = Error

error가 있을때 except문 실행.

---

# 1110

```python
n = input()
n_0 = n[0]
if len(n) == 2:
    n_1 = n[1]
else:
    n_1 = '0'
r = 0
while True:
    s = int(n_0) + int(n_1)
    last = n[1]+str(s)[-1]
    r +=1
    if int(n) == int(last):
        break
```

```python
n=input()
s=0
r=0
while True:
    for i in range(len(n)):
        s+=int(n[i])
    ans = n[-1]+str(s)[-1]
    r+=1
    if int(n) == int(ans):
        break
        print(r)
```

### 정답

```python
n = n_0 = int(input())
r = 0

while True:
    s = n//10 + n%10
    n = int(str(n%10) + str(s%10))
    r += 1
    if n == n_0:
        break
print(r)
```

- 변수 타입

- 자릿수 더하기 : for문, 목적어와 나머지
