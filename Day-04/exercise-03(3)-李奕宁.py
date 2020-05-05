from math import sqrt

num = int(input("请输入一个整数:"))
end = int(sqrt(num))
if num <= 1:
    print(num,"不是质数")
else:
    is_prime = True
    for x in range(2,end+1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print("%d是质数" % num)
    else:
        print("%d 不是质数" % num)
