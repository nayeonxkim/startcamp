# 푸키먼 게임 만들기
# 가상 세계에 동물들이 존재
# 동물들은 각각 고유의 lv, hp, skill, info를 가진다.
# 두 동물이 만나면 한 동물의 hp가 0이 될 때까지 싸운다.

# 공통 속성을 가진 객체를 정의한다
# 클래스명 정의는 Pascal Case로 한다. (단어기준으로 앞글자를 대문자로)
class Pokemon():
    # Class 변수 : 모든 인스턴스가 공통으로 가지는 속성, 모두 접근가능
    info = '푸키먼입니다.'
    population = 0

    # 인스턴스 메서드
    # 매직 메서드 -> __함수명__
    # 그 중 생성자
    # 함수 정의와 동일한 규칙이 적용됨
    def __init__(self, name, lv=1):
        # 인스턴스 변수 self.name
        self.name = name
        self.lv = lv
        self.skill = ('몸통 박치기', 10)
        self.hp = 100

        self.info = self.name[:2] * 2
    # 인스턴스만 접근가능한 인스턴스 메서드
    def attack(self):
        print(self.info)
        return self.skill[1]

    @classmethod
    def increase(cls):
        cls.population += 1 

    # 인자로 self, cls 둘 다 오지 않는 메서드
    @staticmethod
    def battle(pok1, pok2):
        while True:
            pok2.hp -= pok1.attack()
            if pok2.hp <= 0:
                return f'{pok2.name}이 쓰러졌다!'
            pok1.hp -= pok2.attack()
            if pok2.hp <= 0:
                return f'{pok1.name}이 쓰러졌다!'
                
    
        
pika = Pokemon('피카츄')
meta = Pokemon('메타몽', 5)

# 인스턴스 변수가 우선되어 반환

# print(pika.hp)
# Pokemon.battle(pika, meta)