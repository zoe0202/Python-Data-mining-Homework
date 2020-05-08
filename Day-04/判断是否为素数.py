num = int(input("请输入要判断的正整数："))
flag = 0

if num < 2 :
	flag = 1
elif num == 2:
	pass
else:
	for i in range(2,num):
		if num % i == 0:
			flag = 1
			break

if flag == 0:
	print("是素数")
else:
	print("不是素数")
