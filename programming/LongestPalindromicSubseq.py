# Longest palindromic subsequeces using LCS (longest common subsequence in two strings)


def lps(st, rst):
	print("in LPS")
	m = len(st)
	n = len(rst)
	L = [[0 for x in range(m+1)] for y in range(n+1)]

	for i in range(m+1):
		for j in range(n+1):
			if(i==0 or j==0):
				L[i][j] = 0
			elif st[i-1] == rst[j-1]:
				L[i][j] = 1+L[i-1][j-1]
			else:
				L[i][j] = max(L[i][j-1], L[i-1][j])

	print("max:")
	print(L[m][n])

	# now print the resultant string
	list = ""
	i = m
	j = n
	while(i > 0 and j > 0):
		# if current characters are same they are part of LCS
		if(st[i-1] == rst[j-1]):
			#list.append(st[i-1])
			list = list + st[i-1]
			i = i-1
			j = j-1
		elif L[i-1][j] > L[i][j-1]:
			i = i-1
		else: j = j-1

	print(list)
	return st



# Driver program
st = "GEEKSFORGEEKS"
rst = st[::-1]
print("revesed: ")
print(rst)
res = lps(st, rst)
print("Longest palindromic subsequence is: ")
print(res)
