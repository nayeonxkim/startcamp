import requests

name=input('이름이 뭐니?\n내 이름은: ')

r = requests.get(f'https://api.agify.io/?name={name}').json()
age = r['age']
print(f'{name}의 나이는 {age}입니다.')