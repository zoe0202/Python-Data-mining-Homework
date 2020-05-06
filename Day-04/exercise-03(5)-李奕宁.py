x = int(input("x = "))
y = int(input("y = "))
if x>y:
    x,y = y,x
for factor in range(x,1,-1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d不为互质数" % (x,y))
        break
    else:
        print("%d和%d为互质数" % (x,y))
