a = int(input("请输入一个正整数："))
is_prime = True
while a >= 1:
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break
    if a != 0 and is_prime:
        print('%d是质数' % a)
    else:
        print('%d不是质数' % a)
else:
    print("您的输入有误")
