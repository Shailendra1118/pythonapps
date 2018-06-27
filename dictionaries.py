#dictionaries

squars = {1:2, 2:4, 3:9}
squars[8] = 64
squars[3] = 99
print(squars)

print(squars.get(2))
print(squars.get(777, "Not in there idiot"))


# Tuple - similar to List but IMMUTABLE	
words = ("hello", "is","just", "a","word") # not like list {}
print(words)
print(words[1])

#words[0] = "new value" ERROR


list = ["hello","Mr"]
dict = {"hello":"Hello","Mr":"Mr."}
tuple = ("Hello", "Mr")
print(list[0])

print(dict["hello"])
dict["Mr"] = "David"
print("After setting Mister")
print(dict["Mr"])
print(tuple)


# LIST slicing up
list = [12,4,1,4,5,6,7]
print("list[2:]")
print(list[2:]) # start index including, last index excluding
print("list[:2]")
print(list[:2])

