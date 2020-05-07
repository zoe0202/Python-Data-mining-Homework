def fibo(n):
    n1,n2,n3 = 1,1,1
    if n < 1:
        print('输入错误！')
        return -1
    while n > 2:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3

if __name__=='__main__':
    n = int(input("请输入您想计算的斐波那契数列的 n 值：")) 
    print ("计算结果为：",fibo(n))
            
    
 
    
    
