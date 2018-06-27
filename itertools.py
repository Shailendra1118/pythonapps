from itertools import product

# towork with Iterables
# e.g. takewhile, chain, accumulate

a = {1,2}
print(list(product(range(3),a)))
print(len(list(product(range(3),a))))


print("range")

for b in range(2):
	print(b)