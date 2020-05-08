row = 1

while row <= 9:
	for i in range(1,row+1):
		print(i,"*",row,"=",row*i,end="  ")
	print("")
	row += 1