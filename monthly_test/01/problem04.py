def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
   
    try:
        last_id = int(user_data['id'][-1])
        return True
    except:
        return False

# user_data 딕셔너리의 id의 마지막 문자를 정수로 변환합니다.
# 마지막 문자가 정수가 아니라면 int()함수를 적용할 때 ValueError가 발생합니다.
# 따라서 try-except문을 사용하여 error 발생시 False를, 정상인 경우 True를 반환합니다.
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False