
def label(func):
    def wrapper(name):
        print(name, end=' : ')
        func(name)
    return wrapper
# 함수를 받아서 함수를 반환하는 함수 (?ㅋㅋ)

@label
def professor(name):
    print(f'반갑네 {name}교수일세')
    print(f'연구는 잘 되어가나?')



professor('홍')