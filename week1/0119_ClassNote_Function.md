# 함수 응용

#### map(function, iterable)

- iterable 객체의 요소에 하나씩 함수를 적용시킨 결과를 반환하는 함수

- 함수 : () 생략하고 함수 이름만. **호출이 아니라 함수 자체를 넘겨줘야함.**

- **iterable : str, list, tuple, range, set, dict**
  
  - `map(int, list)`
  
  - `map(ord, str)`

- **결과값은  map으로 반환하기 때문에 리스트나 변수 하나에 할당해주어야한다.**

<mark>**질문 :** .함수() 얘네는 왜 안됨?</mark>

- 일단 한번 해보자

<mark>**질문 :** 함수(리스트) , 리스트.함수() 차이점?</mark>  

- <span style='color:gold'>**.함수()** 는 특정 객체(리스트, 문자열 등)에서만 사용가능한 함수들임, 그래서 '메서드' 라고 따로 이름지어 부름.</span>

---

#### filter(function, iterable)

- iterable 객체의 요소에 하나씩 함수를 적용시켜서 결과가 True인 요소들을 모아서 반환하는 함수

- 사용자정의 함수를 넣어서 True를 반환하여서 사용하면 됨.
  
  - ```python
    def odd(n):
        return n % 2
    
    numbers = [1,2,3]
    res = filter(odd, numbers)
    print(list(res))
    >>> [1,3]
    ```

- **결과값은  filter로 반환하기 때문에 리스트나 변수 하나에 할당해주어야한다.**

---

#### zip(iterables)

- 여러 iterable객체들을 같은 자리의 요소끼리 튜플로 저장하여 반환하는 함수
  
  - ```python
    name_list = ['김나연', '김현빈', '구희영']
    age_list = [25, 27, 26]
    
    print(list(zip(name_list,age_list)))
    >>> [('김나연', 25), ('김현빈', 27), ('구희영', 26)]
    ```

---

#### lambda 매개변수 : 리턴값

- def 함수를 더 간단하게 이름없이 정의하는 함수

- 변수에 할당하여 사용 가능
  
  - ```python
    # 바로 함수 사용
    rlt = (lambda x : x * x)(4)
    print(rlt)
    >>> 16
    # 함수를 변수에 할당하여 사
    my_func = lambda n : n * 2
    my_func(2)
    >>> 4
    ```

---

#### 재귀함수

- 자기자신을 호출하는 함수 → 무한반복

- 왜 쓰냐? for, while보다 재귀함수 로직이 더 편할 때가 있음

- 5! = 5 x 4 x 3 x 2 x 1

- n! = n x (n-1)!
  
  - ```python
    def fac(n):
        if n == 0:
            return 1
        return n * fac(n-1)
    fac(5)
    ```

- return에서 자기자신 fac()을 계속 호출하고 있다.

- **재귀함수는 언제 끝날지 명시해주어야한다.**

- **가장 마지막에 호출된 함수부터 실행된다.**

- <span style = 'color:salmon'>**break는 for나 while같은 반복문을 멈출때만 사용. 사용자 정의함수에서는 return으로만 멈춘다.**</span>

- 계속해서 반복실행하기 때문에 로직으로 머리로 그리기 어렵다는 단점이 있다. 
  
  - 그림그려서 로직 이해하고 사용하기!

---

# 패킹/언패킹 연산자 *

- 리스트로 패킹해줌

- 패킹된 객체들은 개별 요소로 풀어줌

#### 포지셔널 가변인자 *

- **사용자정의 함수의 매개변수에 패킹 연산자를 사용해주면, 매개변수 개수를 몇개를 넣든 함수 실행 가능 : 매개변수의 개수를 가변적으로 받을 수 있다. = 가변인자 사용가능 (리스트, 튜플, 그냥 하나의 값 어떤 것이든 상관 없음)**
  
  - ```python
    def test(*values):
        for value in values:
            print(value)
    
    test(1)
    test(1,2,3)
    >>> 1
    1, 2, 3
    
    # 매개변수 하나는 무조건 받겠다.
    def test(a,*values):
        print(a)
        for value in values:
            print(value)
    ```

#### 키워드 가변인자 **

- 키워드 인자를 가변적으로 받는 방법
  
  - ```python
    def test(**kwargs)
    test(name='나연',age=25)
    ```

- 포지션과 키워드 가변인자를 둘 다 사용하는 법
  
  - ```python
    def test(*args, **kwargs)
    test(1,2,3,name='나연',age=25)
    ```

---

# 모듈과 패키지

- 파이썬 파일 하나 (.py)를 모듈이라고 한다.

- 다양한 함수 및 변수를 하나의 파일로 생성한 것이 <span style='color:skyblue'>**모듈**</span>이다.

- 다양한 파일을 하나의 폴더로 생성한 것이 <span style='color:skyblue'>**패키지**</span>다.

- 여러 폴더를 하나로 묶어둔 상위 폴더가 <span style='color:skyblue'>**라이브러리**</span>다.

- 한 모듈에서 하나의 함수만가져오고 싶을 때
  
  - `from 패키지 import 모듈` or `from 모듈 import 함수`
  
  -  <span style='color:salmon'>이렇게 가져오면 `module.function()` 대신 `function()`으로 사용가능!</span>

#### 가상환경 설정할때

- 가상환경? 원하는 버전의 패키지만 사용할 수 있다.

- 집이랑 강의장에 똑같은 가상환경을 설정하고 싶다면, 친구와 내 컴퓨터에 똑같은 환경을 설정하고 싶다면

- 해당 가상환경에서 `pip freeze > requirements.txt` 내가 가진 패키지 목록을 버전과 함께 txt파일로 정리

- 해당 txt파일을 다운받고 `pip install -r requirements.txt`하면 한꺼번에 설치가능

#### 모듈과 패키지 생성하기

- 패키지 생성 : 폴더를 만들고 해당 폴더에 `__init__.py` 파일을 생성한다. (_ 두 개씩) 
  
  - 내용 아무것도 없어도 됨.
  
  - 해당 파일이 있으면 자동으로 그 폴더를 패키지로 인식한다.

- 모듈 생성 : 패키지 폴더 안에 `.py` 파일로 모듈(원하는 함수들을 저장)을 생성한다.
  
  - 안에 자주쓰는 사용자 정의함수들 정의해두면 됨.


