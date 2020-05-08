a = int(input("请输入任意正整数："))
if a == 1:
    print ("1既不是素数也不是质数")
else:
    m = True
    for x in range(2,a):
        b = a%x
        if b == 0:
            m = False
            break
    if m:
        print ("%d是质数" % a)
    else:
        print("%d不是质数" % a)

