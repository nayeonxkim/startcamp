class IBA():

	position = '일반부원입니다.'
	member = 0

	def __init__(self, name, major, pre_course=0):
		self.name = name
		self.major = major
		self.pre_course = pre_course
		IBA.recruit()

	@classmethod
	def recruit(cls):
		cls.member += 1

	@classmethod
	def get_member(cls):
		print(cls.member)

member1 = IBA('Meeseeks', 'Business', pre_course=1)
member2 = IBA('Heundoonge', 'Design')

IBA.get_member()