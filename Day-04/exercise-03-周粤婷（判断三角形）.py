print("判断任意三个数字能否构成三角形，请输入a,b,c的值：\n")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a+b>c and a+c>b and b+c>a:
    print("a,b,c可以构成三角形")
else:
    print("a,b,c不能构成三角形")

