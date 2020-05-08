s = 0
a = int(input('请输入一个整数'))
for x in range(2,a):
    if a % x == 0:
        s+=1
if s == 0:
    print('这是一个质数')
else:
    print('这不是质数')




