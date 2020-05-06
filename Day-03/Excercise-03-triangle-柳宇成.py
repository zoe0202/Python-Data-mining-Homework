a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('可以构成三角形')
else:
    print('不能构成三角形')
