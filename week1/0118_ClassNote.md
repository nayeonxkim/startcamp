# 0118_ClassNote

# 함수

## 분해

`len([1,2,3])` : 리스트의 길이를 넘겨주는 역할을 하는 함수 len()]

---

## return

- return을 적지않으면 눈에 보이진 않지만, `None` 을 반환함.

- <span style='color:salmon'>print와 return은 다르다. print는 테스트를 위해서만 사용</span>  

- print만 있는 함수의 경우, 결과를 변수에 할당하면 None이 저장된다.

```python
def A(x):    
    print(x)

A(a)
>>> a # None
# return없이 print만 했기때문에 콘솔창에 결과는 뜨지만 데이터로 남아있지 않다.
```

    ---

- return을 만나면 함수가 종료된다. 

- <span style='color:salmon'>중간에 return이 있으면 거기서 종료됨!</span> 아래에 있는 코드는 실행되지 않는다.

    ---

- return은 항상 하나의 값만 반환한다.

- 두 개 이상의 값을 반환하려면?

- `return x-y, x*y` : 반환값이 튜플로 묶여서 한 개로 나옴

- `return [x-y, x*y]` : 반환값이 리스트로 묶여서 한 개로 나옴.

---

## parameter와 argument

- 파라미터 : 함수를 정의할 때, 함수 내부에서 사용하는 변수

- 아규먼트 : 함수를 호출할 때, 넣어주는 값

```python
def func(x):
    return x


func(a)
>>> 'a'
```

- x는 parameter, a는 argument

---

## argument의 종류

- Positional Arguments
  
  - 자리로 값을 대입하는 아규먼트
  
  - `func(a, b)`

- Keyword Arguments
  
  - 직접 변수의 이름으로 전달하는 아규먼트
  
  - `func(x=a, y=b)`

- Default Arguments Value
  
  - 기본값을 지정하여 호출 시 argument값을 설정하지 않도록함
  
  - <span style='color:salmon'>기본값이 있는 argument가 뒤에 와야함.</span>
  
  - `def func(x, y=0)` → `func (a)` 
  
  - y=0으로 default를 설정해두어서, 따로 y값을 설정하지 않아도 호출가능
  
  - <span style='color:salmon'>default값이 있어도 원하는 y값으로 넣어줄 수 있음</span>

---

## Name Space

- `A = 10` 할당연산자(=)로 변수에 값을 할당하면, Name Space에 `{'A':10}` 같은 딕셔너리 형태로 기억해둔다.

- Name Space : 어떤 식별자에 어떤 값을 할당하면, 그것을 저장하는 공간

---

## Name Space의 종류

- **Built - in** Namespace : return, list, dict

- **Global** Namespace : .py가 실행될 때, 생성되는 공간

- **Enclosing** Namespace : 중첩함수에서 안쪽 함수를 감싸고 있는 바깥 함수의 local name space
  
  - ```python
    def A():
        def B()
    ```
  
  - A()의 local namespace = enclosing namespace

- **Local** Namespace : 어떤 함수를 실행할 때, 함수 내에 생성되는 공간

---

- <span style='color:salmon'>이름을 저장하는 공간 (Namespace)이 여러개 = 같은 이름이 여러개 존재할 수 있다!</span>

- 네 가지 공간에 같은 이름들이 들어가있을 수 있다.

- 그럼 A가 4개 있다고 가정하자, A를 호출했을 때 파이썬은 어떤 A를 가져올까?

- 이때 등장하는 개념이 scope이다.

---

## Scope

- scope : 내가 찾는 변수가 존재하는 프로그램 상의 범위

- <mark>변수를 찾는 순서 : L E G B</mark>

- 함수를 생성하면 함수 코드 내부에는 local scope가 생성되고, 그 외 공간은 global scope로 구분된다.
  
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능

- 변수
  
  - global variable : global scope에 정의된 변수
  
  - local variable : local scope에 정의된 변수

- 변수의 수명주기 (lifecycle)
  
  - built-in : 파이썬 실행 이후 영원히 유지
  
  - global : 모듈 (py)이 실행된 시점부터 끝날때까지 유지
  
  - local : 함수가 실행될 때 생성되고, 종료될 때까지 유지

```python
# 함수 정의
x = 1 # 글로벌 변수

def func1():
    print('func1')

    def func2():
        print(x)    # L에서 x찾는데 없음 → E → G에서 찾음
        return

     func2()
     return

# 호출
func1()
>>> 
func1
1
```

```python
# 함수 정의
x = 1 # 글로벌 변수

def func1():
    x = 2

    def func2():
        print(x)    # L에서 x찾는데 없음 → E에서 찾음
        return

     func2()
     return

# 호출
func1()
print(x)
>>> 
func1
2         # enclosing의 x를 반환
1         # global에서 x를 호출했으므로 global 변수 x를 불러옴
```

---

- `locals()` : 해당 local scope에서 정의한 모든 변수를 보여줌

- `globals()` : global scope에서 정의한 모든 변수를 보여줌

- <span style='color:salmon'>매개변수(parameter)도 해당 local 변수가 된다.</span>

- `global 변수` : 함수 안에서 사용하면 local이 아닌 global 변수를 가져온다. 
  
  - <mark>**global 함부로 쓰지 말것** : 알고리즘할 때만 최소한으로 사용할 것</mark>

- `nonlocal 변수` : enclosing 변수쓰고 싶을 때. local도 아니고, global도 아닐 때, 해당 scope을 감싸고 있는 가장 가까운 scope에서 변수를 찾는다.

# <mark>질문</mark>

---

- <mark>함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 사용할 것</mark>

# <mark> 질문 : 어떻게?</mark>

---

## 재귀함수
