for i in range(1,10):
    for j in range(i):
        j=j+1
        print("%d*%d=%d"%(j,i,j*i),end=' ')
    print('')