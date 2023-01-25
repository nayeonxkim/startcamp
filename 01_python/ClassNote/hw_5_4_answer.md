# 실습실 hw_5_4

### 제너레이터

```python
def fn_d(n):
    res = n
    while n != 0:
        res += n % 10
        n = n // 10
    return res

print(fn_d(91))
>>> 
```

- 재귀로 만들어보기

#### 셀프넘버

```python
def is_selfnumber(m):
    for i in range(1, m+1):
        if fn_d(i) == m:
            return False
    return True
```

- m의 제너레이터가 될 수 있는 수는 1부터 m까지 중에 있다.
  
  - 1부터 m까지 확인한다.

- 제너레이터가 있으면! 셀프넘버가 아니므로 False로 반환한다.

- 반복문을 다돌았는데도(제너레이터가 나올 수 있는 모든 범위의 수에서 제너레이터를 찾았는데도!) 제너레이터가 없다면 셀프넘버가 맞으므로 True를 반환한다.

```python
# fn_d(n) 정의하지 않고 lambda 사용

def is_selfnumber(m):
    for i in range(1, m+1):
        fn_d = lambda n: sum([int(char) for char in str(n)] + [n])
        if fn_d(i) == m:
            return False
     return True 
```

- 문자열로 바꿔서 각 자리수를 순회하며 더하기
  
  - '1234' -> '1', '2', '3', '4'
  
  - `[int(char) for char in m]`  => `[1,2,3,4]` => `+ [m]` => `sum([1,2,3,4,m])`

----

<mark>`else: return True`하면 안되는 이유?</mark>

`all()` : 하나라도 False면 False

`any()` : 하나라도 True면 True

---

```python
def sum(n):
    if n ==5:
        return True
    else:
        sum(n+1)
```

이렇게하면 결과가 None

sum(n+1) 앞에 return 달아줘야 True반환함
