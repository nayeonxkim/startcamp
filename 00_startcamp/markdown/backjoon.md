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

- 리스트끼리 연산은 +만 된다.

- 리스트 요소를 리스트 빼고, 공백을 넣어서 출력하기 → for문 사용

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

---

# 8958

```python
T = int(input())
for i in range(T):
    ipt = input()
    ls = []
    for j in range(len(ipt)):
        ls.append(ipt[j])
    point = 0
    p_ls = []
    for j in ls:
        if j == "O":
            point += 1
            p_ls.append(point)
        else:
            point = 0

    print(sum(p_ls))
```

- 문자열로 입력받음

- 각 문자열 요소 리스트로 저장

- O일 때 point 1점씩 높이고 모두 리스트로 저장

- 리스트 요소의 합

- else에 pass하면 실행안됨

---

# 2675

```python
T = int(input())
for n in range(T):
    r,s = input().split()
    r = int(r)
    s_lst = []
    for i in range(len(s)):
        s_lst.append(s[i])
    s_lst.apply(x lambda x*r)
    for i in range(len(s)):
        s_lst[i] = s_lst[i]*r
        ans = ''.join(s for s in s_lst)
    print(ans)
```

- `리스트.append(추가할 요소)`

- `''.join`

---

# 1152

```python
setence = list(input().split())
print(len(sentence))
```

---

# 2908

```python
A,B = input().split()
a_lst = []
b_lst = []
for i in range(len(A)):
  a_lst.append(A[i])
  b_lst.append(B[i])
a_lst.reverse()
b_lst.reverse()

for i in range(len(A)):
  A = ''.join(s for s in a_lst)
  B = ''.join(s for s in b_lst)
print(max(A,B))
```

- `리스트.reverse()` : 리스트를 반대로 정렬

---

# 11654

```python
ipt = input()
print(ord(ipt))
```

- `ord()` : 문자열을 아스키코드로 변환

---

# 1157

- 단어 받음 AaB

- 단어 하나씩 리스트로 [A, a, B]

- 대문자로 변환 [A, A, B]

- 아스키코드로 변환 [65, 65, 66]

- cnt 리스트 생성 [0,0,0]

- 아스키코드[i- 65] 나오면 cnt[i]+=1

- cnt 제일 많은거

- 두 개면 ? 

- 아스키코드 -> 알파벳으로 변환해서 출력

```python
word = input().upper()
word_lst = []
for i in range(len(word)):
    word_lst.append(ord(word[i]))
### 단어를 대문자로 받음
### 한글자씩 아스키코드로 리스트 저장.

cnt = [0]*26
for i in word_lst:
    cnt[i-65]+=1
### 알파벳 개수 리스트 생성
### 각 알파벳의 아스키코드가 cnt의 인덱스가 됨: A(65) → cnt[0]
### 따라서 알파벳에 해당하는 인덱cnt[i-65]가 1씩 증가하게 함.

mx = max(cnt)
mx_lst=[]

for i in cnt:
  if i>=mx:
    mx_lst.append(cnt.index(i))
### cnt 값이 최대인 index, 즉 개수가 최대인 알파벳이 여러개인 경우를 대비하여
### cnt가 최대인 인덱스값을 리스트로 저장한다.

if len(mx_lst)>=2:
  print('?')
else:
  print(chr(mx_lst[0]+65))
### cnt최대값이 두 개인 경우 ?를, 하나인 경우 해당 값을 알파벳으로 변환하여 출력
```

<mark>cnt의 인덱스 + 65 = 알파벳의 아스키코드!</mark>

- cnt의 '값'은 해당 알파벳이 몇 번 나왔는지를 뜻하고,

- cnt의 '인덱스'가 알파벳의  아스키코드, 즉 어떤 알파벳인지를 뜻한다.

---

# 1316

```python
# 단어 개수
T = int(input()) 

x_group = 0
#단어 각각 실행하여 반복한다. 전체 과정을 T번 반복
for t in range(T):    
    word = input()                  
# 글자수-1번 반복하여, 앞 글자와 뒷 글자가 다른지 확인한다.      
    for i in range(len(word)-1):    
      if word[i] != word[i+1]:      
        n_word = word[i+1:]        
        if word[i] in n_word:       
            x_group += 1
            break            

print(T-x_group)
```

<mark>같은 알파벳X, 다른 알파벳일 때를 기준으로</mark>

- 단어 한글자씩 확인 aabpba

- 뒷 글자랑 다르면 그 뒷 글자부터 새로운 단어 만들기 bpba

- 해당 회차 글자가 새로운 단어에 있는지 확인 a in bpba ?

- 있으면 그룹단어아님+1

- 전체 단어수 - 그룹단어아님

- <span style='color:tomato'>**break** : break가 속한 가장 가까운 for문을 종료함. </span>

- <span style="color:salmon">만약 같은 단어가 두 번씩 따로 나오는 단어의 경우, (aicpai는 a와 i 두 글자가 두 번씩 나옴) 글자 하나하나에 반복하는  for문 안에 x_group+=1이 들어있으므로 한 글자에 2씩 추가된다. 따라서 한번 추가를 했으면 break로 반복문을 빠져나오게 하여 1씩 추가되게 한다.</span>

---

# 사전학습 중 최빈값

```python
T = int(input())
cnt = [0]*101
for t in range(1, T+1):
    t_num = int(input())
    score_lst = map(int,input().split())
    for i in score_lst:
        cnt[i]+=1
    mx = max(cnt)
    mx_lst = []
    for i in cnt:
        if i>=mx:
            mx_lst.append(cnt.index(i))
    print(max(mx_lst))
```

```python
T = int(input())

for t in range(1, T+1):
    t_num = int(input())
    score_lst = map(int,input().split())
    cnt = [0]*101

    for i in score_lst:
        cnt[i]+=1
    mx = max(cnt)
    mx_lst = []
    for i in cnt:
        if i>=mx:
            mx_lst.append(cnt.index(i))
    print(f'#{t} {max(mx_lst)}')
```

---

# 10809

```python
word = input()

alpha = [-1]*26
ord_lst = []
for i in range(len(word)):
    ord_lst.append(ord(word[i]))
    if alpha[ord_lst[i]-97] == -1:
        alpha[ord_lst[i]-97] = i
    else:
        pass

print(*alpha)
```

- 알파벳 각각을 의미하는 리스트 생성: 인덱스 = 아스키코드 연결되도록

- 단어 입력 받음 baz

- 한 글자씩 아스키코드로 변환 [98, 97, 122]

- alpha[값-97]인덱스에 inex(값) 추가

- <mark>소문자 아스키코드 : 97~122</mark>

- <mark>대문자 아스키코드 : 65~90</mark>

- <span style='color:salmon'>print(*lst) : 리스트를 []와 , 빼고 요소만 출력</span>

---

# 5622
