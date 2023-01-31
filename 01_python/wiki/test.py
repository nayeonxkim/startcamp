class Person:
	def __init__(self):
        self._id = '990916-1234567'

	@property
	def id(self):
        return self._id[:8] + '*'*5



# 데코레이터를 사용하여 메서드를 변수처럼 불러와서 사용
p1 = Person()
print(p1.id)