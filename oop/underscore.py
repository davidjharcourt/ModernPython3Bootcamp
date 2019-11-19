# dunder = underscore on both sides

class Person:
	def __init__(self):
		self.name = "Tony"
		# shows but does not constrain private use
		self._secret = "hi!"
		# python will mangle/change name of attribute
		self.__msg = "I like turtles"

p = Person()

print(p.name)
print(p._secret)

print(p._Person__msg)