import requests

T = input('확인하고 싶은 로또 회차를 입력해주세요!\n: ')

r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={T}').json()
num = list([r['drwtNo1'], r['drwtNo2'],r['drwtNo3'],r['drwtNo4'],r['drwtNo5'],r['drwtNo6']])
print(f'{T}회차 당첨번호는 {num}입니다.')

b = input('보너스 번호를 알려드릴까요? (Y/N)\n:')
bonus = r['bnusNo']
if b == 'Y':
    print(f'보너스 번호는 {bonus}입니다!')
else:
    pass