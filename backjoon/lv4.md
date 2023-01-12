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

<mark>리스트끼리 연산은 +만 된다.</mark>

리스트  요소를 리스트 빼고, 공백을 넣어서 출력하기 → for문 사용
