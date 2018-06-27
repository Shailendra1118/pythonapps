# string, integer and floats
print('2'+'3')
print(int('2')+int('3')) # int is function like float() and str()

print(str(100))
print(float(20))

x = 5;
print(x+2)

#variables
#Python is a case sensitive programming language

lastName = "Yadav"
print(lastName)
#print(lastname) error

#a-name="hello" only _ is allowed in variable names alsong with number and string

print(None) # similar to null, In python it is an object
None
print("printing Null")
# None is return default by function returning nothing
def doSomething(value):
	print("Doing something with "+value)

var = doSomething("Dave");
print(var)

# More types
# dictionary
# Only immutable objects can be used as keys to dictionaries.
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["John"])
# print(ages["Maya"]) throws KeyError
print(ages.get("Maya")) # returns None
print(ages.get("Shailendra", "Yadav")) # why would anyone use that

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

# Tuples similar to list but immutable
words = ("spam", "eggs", "sausages",)
print(words[0])


# [] list {} dictionary () tuple

# Slicing the list
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1]) #excluding last

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# third param
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])


# Negative values
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
print(squares[::-1])

# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.

# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)


