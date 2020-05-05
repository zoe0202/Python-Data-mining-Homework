for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j),end ="\t")#一行当中每两个算式之间空格
    print()#当一行输完以后自动换行
   
