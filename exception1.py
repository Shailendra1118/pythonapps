# raising exception
print(1)
# raise ValueError
print(2)

try:
	na = 23
	va = na/0
except ZeroDivisionError:
	print("divde by zero")
	raise ValueError # simple raise can be used to raise same exception