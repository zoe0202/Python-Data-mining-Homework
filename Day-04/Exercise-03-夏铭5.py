a=int(input('请输入正整数a:'))
b=int(input('请输入正整数b:'))
m=min(a,b)
n=max(a,b)
z=m&n
while z!=0:
    m=n
    n=z
    z=m%n
if z==1:
    print('a,b两数互质')
else:
    print('a,b两数不互质')