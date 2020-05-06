def getname(str1):
    a=int(str1.rfind("."))
    if a<0:
        print("输入错误")
    else:
        print("后缀名是",str1[a:])
str1=input("请输入文件名")
getname(str1)
