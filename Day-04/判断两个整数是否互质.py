num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
flag = 0

if num1 > num2:
	num,num2 = num2,num1

for i in range(num1,0,-1):
	if num1 % i == 0 and num2 % i == 0:
		flag = i
		break

if flag == 1:
	print("互质")
else:
	print("不互质")