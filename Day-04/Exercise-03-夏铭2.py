a=int(input('请输入边长a：'))
b=int(input('请输入边长b：'))
c=int(input('请输入边长c：'))
if a+b>c and a+c>b and b+c>a:
    print('abc三边能构成三角形')
else:
    print('abc三边不能构成三角形')