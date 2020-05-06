''''''
'是否互为质数'
'Author：李斯博'
''''''

a = int(input('请输入第一个大于1的数a='))
b = int(input('请输入第二个大于1的数b='))

tem = 0
while(True):
    tmp=a%b;
 if tem==0:
    break;
else a=b;
    b=tmp
if b==1
    print('a，b互为质数')
    else
    print('a，b不互为质数')



