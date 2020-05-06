#1 百分制成绩转换为等级制成绩
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
else:
    if score >= 80:
       grade = 'B'
    else: 
        if:score >= 70:
            grade = 'C'
        else:
            if:score >= 60:
                grade = 'D'
            else:
                grade = 'E'
print('对应的等级是:', grade)

#输入三条边长判断能否构成三角形
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('可以构成三角形')
else:
    print('不能构成三角形')

#判断是否为质数
from math import sqrt
num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(' %d 是质数' % num)
else:
    print(' %d 不是质数' % num)

#打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print(' ')

#判断是否为互质数
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x and z = x
for i in range(1,z):
    if x%z==0 and y%z==0 and z!=1 :
        print("是互质数")
        break
    else:
        print("不是互质数")