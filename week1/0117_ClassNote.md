# 제어문

### (순차, 선택, 반복) 구조

- 순차 : 위에서부터 아래, 순차적으로 명령수행

- 선택 : 특정 상황에 따라 코드를 선택적으로 실행

- 반복 : 계속해서 같은 것을 반복적으로 실행

---

## 조건문

```python
num = int(input())

if num % 2:
    print('홀수') # 나머지가 1
else:
    print('짝수') # 나머지가 0 : Falsy
```

```python
# 2와 7의 배수의 총합
sum = 0

for n in range(1000):
    if n % 2 == 0:
        sum += n
    elif n % 7 == 0:
        sum += n
print(sum)
```

- <mark>if문에서 True면 elif, else문은 실행 안됨.</mark> (거기까지 안내려옴)

## 조건 표현식 (삼항 연산자)

- if else를 한 줄로 쓰는것

```python
`true일 때 실행할 값` if 조건문 else `false일 때 실행할 값`
```

```python
print('홀수') if n % 2 else print('짝수')
```

---

## 반복문 제어

> `break` : 반복문종료

```python
# break
for n in range(1,11):
    if n == 3:
        break
    print(n)
```

\> 1, 2 출력

- 조건문이 true면 반복문 실행을 멈춤

---

> `continue` : 코드를 실행하지 않지만 반복문은 계속. 바로 다음번 반복으로 넘어감.

```python
# continue
for n in range(1,11):
    if n == 3:
        continue
    print(n)
```

\> 1, 2, 4, 5, 6, 7, 8, 9, 10 출력

- 조건문이 true면 해당 회차는 건너뛰고, 다음 loop로 넘어감.

- 처음 반복문으로 올라감: print까지 가지않고 for문으로 다시 올라가서 실행

- <span style='color:salmon'>break와 달리 반복문은 계속 실행 (조건이 True일때만 건너뜀)</span>

---

> `pass`와 `continue`

```python
# pass
for n in range(1,10):
    if n % 3 == 0:
        pass
    print(n)
```

\> 1, 2, 3, 4, 5, 6, 7, 8, 9 출력

- pass가 있는 해당 조건문만 실행하지 않고 그 다음 코드는 계속 실행

```python
# continue
for n in range(1,10):
    if n % 3 == 0:
        continue
    print(n)
```

\> 1, 2, 4, 5, 7, 8 출력

- continue가 있는 해당 조건문 뿐만 아니라 그 다음 코드도 실행하지 않고 바로 다음 loop실행

- *바로 그 다음 코드 : 반복문 안에 들어있는 코드를 뜻함.

---

> `else` : break로 반복문이 중단된 후, else문 실행

```python
for char in 'apple':
    if char == 'l':
        break
else:
    print('p가 나왔습니다')
```

- 반복문 실행이 모두 끝난 후, else문 실행

- <span style='color:salmon'>break문으로 실행이 종료된 경우에 else문이 실행됨.</span>

---

> `enumerate()` 

```python
members = ['민수','영희','철수']
for idx,n in enumerate(members):
    print(idx,n)
```

- 인덱스도 같이 반환

0 민수
1 영희
2 철수

---

## 리스트 표현식

`[code for 변수 in iterable if 조건식]`

```python
#1~3의 세제곱 리스트 만들기
## for문 사용
cubic_lst = []
for i in range(1,4):
    cubic_lst.append(i**3)

## 표현식 사용
cubic_lst = [i**3 for i in range(1,4)]
```

## 딕셔너리 표현식

```python
#1~3의 세제곱 딕셔너리 만들기
## for문 사용
cubic_dic = {}
for i in range(1,4):
    cubic_dic[i] = i**3

## 표현식 사용
cubic_dic = {i: i**3 for i in range(1,4)}
```
