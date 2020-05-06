A=float(input('请输入第一条边的值'))
B=float(input('请输入第二条边的值'))
C=float(input('请输入第三条边的值'))
if A + B > C and A + C > B and B + C>A:
    print('可以构成三角形')
else:
    print('不可以构成三角形')