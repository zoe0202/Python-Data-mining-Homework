''''''
'三边是否构成三角形'
'Author：李斯博'
''''''

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b>c and b+c>a and a+c>b:
    print('可以构成三角形')
else:
    print('不能构成三角形')
