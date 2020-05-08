'''
打印九九乘法表
'''
for i in range(1, 10):#第一层循环
    for j in range(1, i+1):#第二层循环
        print('{}x{}={}\t'.format(j, i, i*j), end='')#输出一行
    print()#换行