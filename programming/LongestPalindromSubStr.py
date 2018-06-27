import sys

# A utility function to print a
# substring str[low..high]
def printSubStr(st,low,high) :
    sys.stdout.write(st[low : high+1])
    sys.stdout.flush()
    return ''


def longestPalSubstr(st) :
	n = len(st)
	table  = [[0 for x in range(n)] for y in range(n)]
	#print(table)
	#print(np.matrix(A))

	maxLength = 1
	i = 0
	# single char str
	while(i < n) :
		table[i][i] = 1 #1 is True
		i = i+1
	# check for sub-string of length 2
	start = 0
	i=0
	while i < n-1 :
		if(st[i] == st[i+1]) :
			table[i][i+1] = 1
			start = i
			maxLength = 2
		i = i+1

	
	k = 3
	while(k <= n) :
		i = 0 # start index    	
		while(i < (n-k+1)) :
			j = i+k-1 # end index
    		# checking for sub-string from ith index to jth index
            # iff st[i+1] to st[(j-1)] is a palindrome
			if(table[i+1][j-1] and st[i] == st[j]) :
				table[i][j] = 1
				if(k > maxLength) :
					maxLength = k
					start = i
			i = i+1
		# print("incrementing k ", k)
		k = k+1
	# print ("longest palindrome is \n")
	print(maxLength)
	print(printSubStr(st, start, start+maxLength-1))



	# Print the table
	for row  in table :
		for elem in row :
			print(elem, end='')
		print()
	#print("nLength of table is ")
	#print(len(table))


# Driver program to test above functions
st = "forgeeksskeegfor"
l = longestPalSubstr(st)
print("\nLength is:", l)