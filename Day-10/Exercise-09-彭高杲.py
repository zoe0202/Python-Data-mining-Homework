import threading
from time import time, sleep

def baoshu():
    for i in range(10):
        q = i + 1
        print(threading.currentThread().getName()+'报数:'+str(q)+' ')
        sleep(0.5)

def main():
    t1 = threading.Thread(target=baoshu)
    t1.start()
    t2 = threading.Thread(target=baoshu)
    t2.start()
    t3 = threading.Thread(target=baoshu)
    t3.start()
    t4 = threading.Thread(target=baoshu)
    t4.start()
    t5 = threading.Thread(target=baoshu)
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

if __name__ == '__main__':
    main()