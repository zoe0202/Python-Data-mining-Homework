a = float(input("请输入a边的长："))
b = float(input("请输入b边的长："))
c = float(input("请输入c边的长："))

if a+b>c and a+c>b and b+c>a:
	print("能构成三角形！")
else:
	print("不能构成三角形哦！")