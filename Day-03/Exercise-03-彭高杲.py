from math import *

#1. 将用户输入的百分制成绩转换为等级制成绩
score = float(input('Please write your score there: '))

if score>100 or score < 0:
    grade = 'wrong'
elif 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'E'

print('Your grade is: '+grade)

#2. 根据用户输入的三条边的边长，判断三条边是否能够构成三角形
a,b,c = map(float,input('Please input the three sides of your triangle: ').split())
if (a+b>c) and (a+c>b) and (b+c>a):
    print("Yes, it's a triangle!")
else:
    print("We're sorry that it's not a triangle.")

#3. 根据用户输入的整数，判断该整数是否为质数
number_3 = int(input('Please write your integer: '))
if number_3 == 1:
    judge = False
elif 2<=number_3<=3:
    judge = True
else:
    middle = floor(sqrt(number_3))
    i = 1
    for q in range(1, middle):
        i += 1
        if number_3 % i == 0:
            judge = False
            break
        else:
            judge = True
if judge:
    print("Congratulations! It's a prime number!")
else:
    print("It's not a prime number!")


#4. 输出九九乘法表（格式如1×1=1，每行输出一个）到控制台
for i in range(1,10):
    for q in range(1,i+1):
        print(str(i)+'×'+str(q)+' = '+str(i*q)+' ',end='')
    print('')

#5. 判断用户输入的两个整数是否为互质数（最大公因数为1）
e,f = map(int,input('please write your two number there: ').split())
i = 1
test_1 = []
test_2 = []
g = floor(sqrt(e))
for j in range(1,g):
    i += 1
    if e % i == 0:
        test_1.append(i)
    else:
        continue
h = floor(sqrt(f))
i = 1
for j in range(1,h):
    i += 1
    if h % i == 0:
        test_2.append(i)
    else:
        continue
judge_5 = True
for q in test_1:
    if q in test_2:
        judge_5 = False
        break
    else:
        pass
if judge_5:
    print('Yes, they are relatively numbers.')
else:
    print('No, they are not relatively numbers.')


print('-----------------------End----------------------------')