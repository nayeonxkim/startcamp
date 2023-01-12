# dictionary
student = {
    '강남' : '스타일', 
    '강북': '멋쟁이', 
    '종로구': [1,2,3],
    '서대문구' : {'김나연': 99, '김현빈': [96, 97], '구희영':98}
    }
print(student)
print(student['서대문구'])
print(student['서대문구']['김현빈'][0])

# list
menu = [
    ['아침','점심','저녁'],
    {'breakfast': '오트밀', 'lunch': '토마토리조또', 'dinner':'불고기'},
    '잠온다.'
]
print(menu)
print(menu[0][1])
print(menu[1]['lunch'])