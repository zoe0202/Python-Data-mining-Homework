num = int (input("请输入一个整数:"))  
if num <= 1:  
    print("%d不是质数!"%num)  
elif num == 2:  
    print("%d是质数!"%num)
else:  
    t=2  
    while t < num:  
        if num%t == 0:  
            print("%d不是质数!"%num)  
            break  
        t += 1  
    else:  
        print ("%d是质数!"%num)
