class IBA():
	def __init__(self):
		self._age = 0

	@property
	def age(self):
		return self._age
		
	@age.setter
	def age(self, age):
		self._age = age

	

member1 = IBA()
member1.age = 25
print(member1.age)