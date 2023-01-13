import requests

T = input('확인하고 싶은 로또 회차를 입력해주세요!\n: ')

r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={T}').json()

num= []
for i in range(1,7):
    num.append(r[f'drwtNo{i}'])

print(f'{T}회차 당첨번호는 {num}입니다.')

b = input('보너스 번호를 알려드릴까요? (Y/N)\n:')
bonus = r['bnusNo']

if b == 'Y':
    print(f'보너스 번호는 {bonus}입니다!')
else:
    pass
#########################################
import random as rd
import requests

# 로또 당첨 확인 API를 받아옵니다.
r = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()
# 보너스 번호와
bonus = r['bnusNo']
# 6개의 당첨번호를 변수/리스트에 저장합니다.
num= []
for i in range(1,7):
    num.append(r[f'drwtNo{i}'])

# 각 등수별로 당첨된 횟수를 출력하기 위해 리스트를 만들어줍니다.
cnt_lst = [0] * 5

# 1000번 반복을 실행합니다.
t=0
while t<1000:

    # 랜덤 숫자 6개를 불러옵니다.
    my_num = list(rd.sample(range(1,46),6))
    # 당첨번호가 랜덤숫자 리스트에 있는지 확인해줍니다.
        ## 1) 당첨번호를 직접가져와서 확인
    point = 0
    for i in my_num:
        if i in num:
            point+=1
        ## 2) 랜덤숫자를 인덱스로 가져와서 당첨번호 리스트에 있는지 확인
    # for  i in range(len(my_num)):
    #     if my_num[i] in num:
    #         point+=1

        ## 3) 집합으로 만들어서 교집합 확인

    # 당첨번호와 일치하는 번호 개수대로 등수를 출력합니다.
    if point == 6:
        cnt_lst[0]+=1
        print(f"#{t} ((경))********* 1등입니다! *********((축))")
    elif point == 5:
        cnt_lst[1]+=1
        print(f"#{t} 축하합니다, 2등이네요!")
    elif (point == 5) and bonus in my_num:
        cnt_lst[2]+=1
        print(f"#{t} 축하합니다, 3등이네요!")
    elif point ==4:
        cnt_lst[3]+=1
        print(f"#{t} 4등입니다!") 
    elif point ==3:
        cnt_lst[4]+=1
        print(f"#{t} 아쉽군요~ 5등입니다!") 
    else:
        pass

    t+=1

print(f'총 {cnt_lst[0]}번 1등하셨어요.')
print(f'총 {cnt_lst[1]}번 2등하셨어요.')
print(f'총 {cnt_lst[2]}번 3등하셨어요.')
print(f'총 {cnt_lst[3]}번 4등하셨어요.')
print(f'총 {cnt_lst[4]}번 5등하셨어요.')
print('당첨 확인이 끝났어요.')
