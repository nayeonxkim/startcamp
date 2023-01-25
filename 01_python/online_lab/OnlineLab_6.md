# Online Lab 6

## 실습 6_1

> 주민등록번호 앞의 6자리는 생년월일이고,
> 
> 뒤 7자리는 성별, 지역, 오류검출코드이다.    
> 
> 주민등록번호를 입력받아 주민등록번호 뒷자리를 비식별화하는 함수 de_identify 를 만들어라.

### 내 풀이 : isdemical()

```python
def de_identify(id):
    id_lst = []
    for i in id:
        if i.isdemical():
            id_lst.append(i)
    for i in range(6,13):
        id_lst[i] = '*'

    return ('').join(id_lst)
```

- 먼저, 입력받은 문자열에서 정수 0~9만 뽑아서 id_lst에 추가한다.
  
  : isdemical() 은 문자열의 메서드로, 0~9이면 True를 반환한다.

- id_lst의 6번째 문자부터 끝까지 *로 변환한다.

- 구분자 없이 리스트 요소들을 모두 하나로 합쳐 반환한다.

<span style='color:orange'>`isdigit()`은 숫자면 True, `isdemical()`은 0~9만 True</span>

    : `'1.5'.isdigit()` = True, `'1.5'.isdemical()` = False

### replace(), 리스트

```python
def de_identify(id):
    id = id.replace('-','')
    id_lst = list(id)
    id_lst[6:] = '*'*7
    return ('').join(id_lst)
```

- 입력받은 문자열에서 -를 공백으로 대체하여 없앤다.

- 문자열을 리스트로 변환하여, 6번 인덱스부터 7개를 *로 변환한다.

- 구분자 없이 리스트 요소들을 모두 하나로 합쳐 반환한다.

### replace(), 문자열 연산

```python
def de_identify(id):
    id = id.replace('-','')
    censored_id = id[:6] + '*'*7
    return censored_id
```

---

## 실습 6_2

> 작물과 가격이 함께 있는 리스트가 존재할 때, 
> 
> 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
> 
> 단, 작물의 이름을 직접 입력하여 출력하지 않는다.

```python
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

max = 0
for i in range(len(grain_lst)):
    price = grain_lst[i][1]
    if price >= max:
        max = price
        idx = i
print(grain_lst[idx][0])
```

- grain_lst의 모든 요소를 순회하며 확인한다.
  
  - 요소의 [1]값을 price변수에 할당한다.
  
  - price가 max보다 크면 max 를 price로 업데이트한다.
  
  - idx에 해당 price의 인덱스를 할당한다.

- 가장 큰 price를 가지는 idx번째 요소의, [0]값을 반환한다.

### 딕셔너리

```python
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


grain_dict = dict(grain_lst)

key = list(grain_dict.keys())
value = list(grain_dict.values())

max_value = max(value)
max_idx = value.index(max_value)

print(key[max_idx])
```

- 리스트 안에 튜플이 있으면 딕셔너리로 변환 가능

- <span style='color:orange'>딕셔너리에서 value값으로 key값 찾기</span>
  
  - key와 value를 각각 리스트로 저장
  
  - `value.index(찾는 value)` 로 해당 value의 인덱스를 구한다. : 리스트의 메서드 index() 사용
  
  - key 리스트에서 위에서 찾은 인덱스로 해당 value의 key를 찾는다.

### 리스트 : sort()와 lambda

```python
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

grain_lst.sort(key=lambda x : x[1], reverse=True)
print(grain_lst[0][0])
```
