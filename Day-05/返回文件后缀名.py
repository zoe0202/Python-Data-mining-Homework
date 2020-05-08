def suffix(filename):
	for i in filename[::-1]:
		if i == ".":
			flag = filename.index(i) + 1
			return filename[flag:]

name = input("请输入你的文件名：")
print(suffix(name))