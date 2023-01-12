# if 조건문 & for 반복문
dust = [53, 95, 12, 8 , 9, 57, 80]

for i in range(len(dust)):
    if dust[i]>50:
        print(f'#{i} 50초과')
    else:
        print(f'#{i} 50이하')

# if 조건문
d=13
if d>50:
    print('50초과')
else:
    print('50이하')

# if-else 조건문
if d > 50:
    print('over 50')
elif d > 30:
    print('over 30')
else: 
    print('under 30')
    
## 하나의 조건문을 통과하면 그 다음 조건문까지 가지 않음.
## 우선되는 조건을 항상 먼저 생각하기.
