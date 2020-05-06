X=int(input('请输入一个大于1的整数：'))
for Y in range(2,X):
    if X%Y == 0:
        print('这个数不是质数')
        break
    else:
        print('这个数是质数')
        break

