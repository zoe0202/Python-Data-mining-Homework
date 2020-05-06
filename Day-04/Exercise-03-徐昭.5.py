x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
     if x % factor == 0 and y % factor == 0:
         if factor == 1:
             print ('%d和%d互质'%(x,y))
             break
         else:
             print ('%d和%d不是互质数'%(x,y))
             break
    
