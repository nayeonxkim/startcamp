# 파이썬

## 저장

#### 변수에 저장할 수 있는 것

- 숫자, 글자, bool

#### 변수 활용하기

리스트 안에 딕셔너리, 딕셔너리 안에 리스트 가능

for 문 in 딕셔너리도 가능!!!

변수의 모든 요소를 순회하면 끝

in 뒤에 int 올수없음

<mark>→ len(리스트)는 int아님. int처럼 보이는것</mark>

종료조건 필요없음!!

while은 특정 조건을 만족하는 동안 계속, 종료조건 필수!!!

---

### for문에 딕셔너리 사용

```python
# 딕셔너리의 value값 반복 출력
numbers = {'a':1, 'b':2}
for i in numbers:
    print(numbers[i])

# 딕셔너리의 key값 반복 출력
for i in numbers:
    print(i)
```


