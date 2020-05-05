X=int(input('请输入整数1:'))
Y=int(input('请输入整数2:'))
if X > Y:
    X,Y=Y,X
for Z in range(X,1,-1):
    if X%Z==0 and Y%Z==0:
        print('这两个数不是互质数')
        break
    else:
        print('这两个数是互质数')
        break