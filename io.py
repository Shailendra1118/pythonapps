file = open("README.md", "r")
cont = file.read()
#print(cont)
file.close()


file = open("exception1.py", "r")
print(file.read(16)) #read 16 characters
for line in file:
    print(line) #auto added new line
