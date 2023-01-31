from wiki.pokemon import Pokemon
# 코드를 실행을 시킨 상태로 가지고 옴!
# 코드를 실행시켜야 Pokemon함수가 메모리 공간에 할당되어 사용할 수 있기 때문
# pokemon.py의 print가 여기서 같이 실행되는 이유가 이거 때문

class Pika(Pokemon):
    no = 25
    breed_population = 0
    
    def __init__(self, name, lv = 5):
        super().__init__(name, lv)
        self.skill = '전기충격', 25

class Meta(Pokemon):
    no = 13
    breed_population = 0

class Child(Pika, Meta):
    pass


class Brother(Meta, Pika):
    pass

c1 = Child('피카몽')
print(c1.name)
print(c1.skill)

b1 = Brother('메타츄')
print(b1.no)
print(b1.skill)