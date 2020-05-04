def Fahrenheit():
   while True:
      Fahrenheit=input("请输入一个带单位(F/f)的华氏温度值,我们将为您转化为摄氏度：\n")
      if Fahrenheit[-1] in ['F','f']:#判断输入的是否为华氏度
          C = (eval(Fahrenheit[0:-1])-32)/1.8
          print("转换后的温度是{:.2f}C".format(C))
          break
        
      else :
         print("输入错误，请输入正确的华氏度(F/f)!")
Fahrenheit()
