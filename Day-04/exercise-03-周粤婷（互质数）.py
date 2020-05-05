input("请输入两个非零自然数：")
a = int(input("a="))
b = int(input("b="))
n = True
if a>=b:
    m=b
else:
    m=a
for x in range(2,m+1):
    p = a%x
    q = b%x
    if p == 0 and q == 0:
        n = False
        break
if n:
    print("%d和%d是互质数" % (a,b))
else:
    print ("%d和%d不是互质数" % (a,b))
