white = {"zhanghao1":"123","zhanghao2":"789"}#白名单
black = {"heimingdan1":"000"}#黑名单

username = input("请输入账号：")

num = 0

if username in black:
	print("你的账号已经被锁死")
else:
	if username in white:
		while num < 3:
			password = input("请输入密码：")
			if white.get(username) == password:
				print("登陆成功！")
				break
			else:
				print("密码有误（如果连续三次输入错误则自动锁死账号）")
				num += 1
		else:
			print("连续三次输入错误，账号已锁死！")
			black[username] = password
	else:
		print("用户名不存在！")