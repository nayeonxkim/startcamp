def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    # id, password 중 하나라도 빈 문자열이면 False를 반환합니다.
    if (user_data['id'] == '') or (user_data['password'] == ''):
        return False
    # 둘 다 문자열이 있으면 True를 반환합니다.
    else:
        return True

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True