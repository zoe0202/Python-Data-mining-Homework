a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))
while a != b:
    while a > b:
        if a % b == 0:
            print("不是互质数")
        else:
            print("两数为互质数")
        break

    while b > a:
        if b % a == 0:
            print("不是互质数")
        else:
            print("两数为互质数")
        break
    break
else:
    print("不为互质数")
