'''
使用多线程实现5个线程分别报数（每个线程每隔0.5秒报一个数，从1报到10）
'''
from threading import Thread
import time
def number():                              #定义报数函数（进程？
    for i in range(1,11):
        print(i)
        time.sleep(0.5)
def main():                                     #多线程执行 （线程？
    t1=Thread(target=number)        #试了一下 number后加不加（）结果不一样，其实不太清楚原因。。
    t1.start()
    t2=Thread(target=number)
    t2.start()
    t3=Thread(target=number)
    t3.start()
    t4=Thread(target=number)
    t4.start()
    t5=Thread(target=number)
    t5.start()
    t1.join()                                  #join方法表示等待进程执行结束
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print('报数完毕！')
if __name__ == '__main__':
    main()