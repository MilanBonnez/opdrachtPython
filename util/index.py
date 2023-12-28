
class Person:
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def setFirstName(self, firstName):
		self.firstName = firstName

	def setLastName(self, lastName):
		self.lastName = lastName

class Student(Person):
	def __init__(self, firstName, lastName, opleiding):
		super.__init__(firstName, lastName)
		self.opleiding = opleiding

class Teacher(Person):
	def __init__(self, firstName, lastName):
		super.__init__(firstName, lastName)