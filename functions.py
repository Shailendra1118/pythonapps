
def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func() # has to be defined first to use here

def doThis(word):
	return word+"!"

operation = doThis
print(operation("hello"))
print(doThis("boy"))


# function can be passed as arguments to function and returned
def add(x,y):
	return x+y

def twice(func,x,y):
	return func(func(x,y),func(x,y))

print(twice(add,2,3))