# Useful HIGH ORDER FUNCTIONS

a = lambda x:x**2;
print(a(20))

def myFunc(f, args):
	return f(args)

print(myFunc(a,12))

num = [1,2,3,4,5,6];
res = 0
res = list(map(lambda x:x*2,num))
print(res)

res = myFunc(lambda x:x*2,num)
print(res)

#Lambda -short hand to create anonymous functions

ans = filter(lambda x:x>2, num)
print("ans")
print(list(ans))

z = (lambda x:x*(x+1))
print(z(6))

# anonymous function call
y = (lambda x:x**3)(5)
print(y)

