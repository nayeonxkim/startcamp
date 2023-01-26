# 0126_ClassNote_DataStructure

## 데이터 구조란 ?

- 데이터를 효과적으로 저장하고 활용하기 위한 구조

- 자료구조를 학습할 때는 <span style='color:salmon'>데이터 구조</span>와 데이터구조를 활용한 <span style='color:salmon'>연산</span>을 알아야한다.

![](https://t1.daumcdn.net/cfile/tistory/99E4BA415AEB1E9801)

- 플레이리스트 : 곡1 → 곡2 → 곡3 
  
  - 선형적으로 이어짐 : 선형구조 연결리스트

- 팔로잉리스트 : A → B → D → A 
  
  - 비선형적, 위 처럼 표기하기 어려움 : 비선형구조 그래프

---

## 메서드

- 메서드 : 특정 데이터구조의 built-in 함수 `객체.메서드()`
- 파이썬 내장함수 : 파이썬 자체의 내장함수 `내장함수(객체)`

---

### 공식문서에서 메서드 찾아쓰기

`.메서드(key[,default])`

- key : 필수입력값
  
  - key처럼 () 안에 있는 값들을 뜻함

- [] : 선택사항
  
  - [] 안에 있는 내용이 선택적이라는 뜻
  
  - 입력할 때 []는 필요없음

---

## String

- 문자열은 불변형
- 변경 메서드 사용하면 기존 문자열은 그대로, 새로운 문자열을 생성
  - 바꾼 문자열을 계속 사용하려면 변수에 할당해주어야함.

---

### String 메서드

>  주어진 문자열에서 숫자, 문자, 기호가 각각 몇개인지 판단하는 함수 check()을 작성하라. (출력예시 - 문자:10개, 숫자:2개, 기호: 7개)

```python
def check(str):
    char_cnt = 0
    digit_cnt = 0
    symbol_cnt = 0

    for char in str:
        if char.isalpha():
            char_cnt += 1
        elif char.isdigit():
            digit_cnt += 1
        else:
            symbol_cnt += 1
    return (char_cnt,digit_cnt,symbol_cnt)

str = input()
char, digit, symbol = check(str)
print(f'문자 : {char}개, 숫자 : {digit}개, 기호 : {symbol}개')
```

- 문자열이 `문자`인지 확인하는 메서드 : `isalpha()`
  
  - 한글, 영어 다

- 문자열이 `숫자`인지 확인하는 메서드 : `isdigit()`
  
  - 모든 숫자 다
  
  - 0~9 정수인지 확인하는 메서드 : `isdemical()`

- 문자열이 `기호`인지 확인하는 메서드는 따로 없음 !
  
  - 다른 조건을 먼저 판별 후에 `else`로 찾음

---

# Set {}

### <span style='color:salmon'>**중복을 허용하지 않는다.**</span>

- 중복되는 원소는 하나만 저장

### **순서가 없다.**

- 인덱스로 접근 불가능

---

## 딕셔너리

- `dict.get(key)` 메서드와 `dict[key]`의 차이점은 ?
  
  - get 메서드 사용 시, 해당 key 값이 없으면 None이나 설정한 default 값을 반환한다.
  
  - dict[key] 사용 시, 해당 key 값이 없으면 KeyError가 발생한다.
  
  - <span style='color:salmon'>`dict[key]`는 해당 key가 딕셔너리에 있다는 확신을 갖고 사용해야 한다.</span> (if문으로 key 값을 확인하는 등의 절차 필요) `get()`메서드는 그런 절차가 필요없기 때문에 더 간단하게 사용할 수 있다.

- `dict.pop(key[,default])` 메서드를 사용할 때, 해당 key값이 딕셔너리에 없으면?
  
  - 설정한 default값을 반환한다.
  
  - default값을 설정하지 않으면 KeyError가 발생한다.

---

### 리스트와 튜플 메서드 활용

#### 리스트

```python
sample_lst = [11, 22, 33, 55, 44]
print(sample_lst)
#1. 주어진 리스트의 3번 인덱스 있는 항목을 제거하고 변수에 할당하라.
deleted = sample_lst.pop(3)
print(sample_lst)

#2. sample_lst 가장 뒤에 77을 추가하라.
sample_lst.append(77)
print(sample_lst)

#3. 변수에 할당한 값을 sample_lst의 2번 인덱스에 추가하라.
sample_lst.insert(2,deleted)
print(sample_lst)
```

#### 튜플

```python
sample_tuple = (11, 22, 33, 44, 55, 66)
print(sample_tuple)

# 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당하라.
new_tuple = (sample_tuple[3:5])
print(new_tuple)
```

---

## 리스트 메서드

- `리스트.sort()`: 리스트 메서드
  
  - <span style='color:salmon'>기존 리스트 자체를 정렬 !</span>

- `sorted(리스트)`: 파이썬 내장함수
  
  - <span style='color:salmon'>기존 리스트는 그대로</span>, 정렬한 리스트를 새로 생성
  
  - 정렬한 리스트 사용하려면 다른 변수에 할당 필요

- 리스트 변경메서드 → '반환' 도 같이해주는 `.pop()`같은 메서드가 아니면 print했을 때None 반환함.
  
  - `print(lst.sort())`하면 None나옴.

---

# 얕은 복사와 깊은 복사

### 참조 = 주소값

> 0116_ClassNote_Memory와 연결되는 내용

- 문제점 : 하나의 값에 하나의 주소 필요
  
  → 100개를 저장하려면 주소 100개가 필요하다 !

- 하나의 주소에 여러 개 넣을 수 없나 ?
  
  → 연속적인 공간에 데이터를 저장해서 맨 처음 주소만 가지고 있으면 찾을 수 있게 하자!

---

### 얕은 복사

- 복사는 됐는데 같은 주소를 가짐

- 두 변수가 하나의 주소를 가짐 !

- 하나를 바꾸면 다른 하나도 변경됨

### 깊은 복사

- 복사는 하되, 다른 주소를 가지려면?
  
  - 내용만 같고 다른 메모리를 가짐

- 두 변수가 각각의 주소를 가짐 !

- 하나를 바꿔도 다른 하나에 영향 없음

### 얕은 복사와 깊은 복사는 0과 1처럼 딱딱 나누어지는게 아님 !

- slicing 얕은 복사의 경우, 1차원 리스트는 깊은 복사처럼 보인다.

- 애매하게 깊은 복사인 느낌!

---

## 복사방법

### 할당연산자(=) 사용

- =으로 복사하면, 해당 객체에 대한 객체 '참조' 를 복사한다.

- 두 변수가 같은 주소값을 가진다.

### 얕은 복사

- Slicing 사용 : `b = a[:]`

- slicing을 사용하면 두 리스트의 주소는 다르다.

- 그러나, 리스트 in 리스트가 있는 경우, <mark>해당 리스트의 주소</mark>를 공유하기 때문에 얕은 복사임

- 깊은 복사는 이런 '참조의 참조' 까지도 복사되어야한다. (복사 = 다른 주소값을 가져야한다.)

<mark>해당 리스트의 주소 ?</mark>

== 참조의 참조 !

- 하나의 주소엔 무조건 하나의 값만 들어감

- 리스트 요소 각각 하나씩만 저장될 수 있다.

```python
a = [1, 2, ['a', 'b']]
```

- |1|2|`['a', 'b']` 리스트의 첫 주소값| | |'a'|'b'|

### 깊은 복사

- copy 모듈의 `copy.deepcopy(리스트)` 사용

- 참조의 참조 (3차원도, 몇차원이든!) 까지도 모두 복사하여 새로운 주소값에 할당함.

---

## 리스트 끼리의 합

```python
sum([[1,4],[2,3],[5,6]], [])
>>> [1,4,2,3,5,6]
```


