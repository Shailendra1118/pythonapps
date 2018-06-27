#conditions
if (10 > 6):
	print("under if")
	spam = "spam1"
	if(spam == "spam"):
		print("in spam")
	else:
		print("nothing")

else:
	print("in else")


#boolean operator and or and not
if( 1==3 or "hello"=="hello"):
	print("inside boolean eg")

if(not 1==2):
	print("its not")


# == has a higher precedence than or:
# parentheses first, then exponentiation
# Unary operators like complement ~+-
# then multiplication/division, and then addition/subtraction
# then left right bitwise shift
# bitwise AND '&'
# bitwise XOR ^ and OR |
# comparison
# equality
# assignment
# logical like not and or
if(False == False or True):
	print("who has higher precedence, its ==")

if(False == (False or True)):
	print("who has higher precedence?")
else:
	print("In else")



#Loop
i = 0
while i <=5:
	print(i)
	i = i+1

print("done")


# for Loop
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# Prints out 3,4,5
nlist = []
for x in range(3, 6):
    print(x, end=' ')
    nlist.append(x)

print(nlist)

for x in range(1,5): #5 is excluding
	print(x)


