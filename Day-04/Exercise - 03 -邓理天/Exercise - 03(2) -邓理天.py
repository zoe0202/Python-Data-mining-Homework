'''
输入三条边长判断能否构成三角形
'''
a = float(input("请输入第一条边的边长："))
b = float(input("请输入第二条边的边长："))
c = float(input("请输入第三条边的边长："))
if a<b+c and b<a+c and c<a+b:
    print("您输入的边长能构成三角形")
else:
    print("您输入的边长不能构成三角形")