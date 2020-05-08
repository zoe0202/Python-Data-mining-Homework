a = float(input('请输入三角形一边长'))
b = float(input('请输入三角形一边长'))
c = float(input('请输入三角形一边长'))
if a+b>c and a+c>b and b+c>a:
    print('这可以构成三角形')
else:
    print('这不能构成三角形')
L = a+b+c
i = (a+b+c)/2
S = (i * (i - a) * (i - b) * (i - c)) ** 0.5
print('此三角形的周长是'+str(L)+'此三角形的面积是'+str(S))
