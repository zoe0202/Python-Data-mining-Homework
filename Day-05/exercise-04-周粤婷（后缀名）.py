str1 = str(input("请输入完整文件名："))
if "." in str1:
    start = str1.find('.')
    print(str1[start:])
else:
    print("请输入完整文件名！")