class Cat:
	name = "default"
	def __init__(self, color, age):  #constructor
		self.color = color
		self.age = age


	def _init_(self, isDangerous):  # Just as normal method
		self.isDangerous = isDangerous

felix = Cat("Brown", 2)
print(felix.color)
print(felix.name)

bob = Cat("Black", 3)
print(bob.name)
Cat.name = "Bob" # now this name is shared across all instances of CAT
print("name changed-")
print(bob.name)
print(bob.age)

bob._init_(False)
print(bob.isDangerous)

marley = Cat("White", 5)
print(marley.name)
print(marley.color)