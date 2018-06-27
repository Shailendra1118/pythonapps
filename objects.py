words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

empty = [10, 12, 12,] #not error for last comma
print(empty)


#list of list, not 2D array in Python
print("------")
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[0][2])
print(things[2][1])


list = [1,2,3,4,]
list[1] = list[0]
print(list) 

# check in list
items = ["hello", 'Shailendra','yadav', 'Maya']
print("Shailendra" in items) # TRUE
print("Mayo" in items) # FALSE

# in for substring check
print('Shail' in "Shailendra") # true


#List functions
nums = [1, 2, 3]
nums.append(4)
print(nums)

#insert method
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

#index
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
#print(letters.index('z')) throws ValueError

print('before removing')
print(letters)
print('after removing')
letters.remove('u')
print(letters)


#count
print(letters.count('p'))
print('reversed')
print(letters.reverse()) # returns None ??
print(letters)
words.reverse()
print(words)

# another way of reversing the list in Python
L = [0,10,20,40,50]
print(L)
L = L[::-1]

print(L[:-2]) #indexing from the last

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(squares[2:3]) # last index is exclusive, first is inclusive
print(L[2:3])


