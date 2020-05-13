from threading import Thread,Lock
from time import sleep
import threading
lock=threading.Lock()
def count():
    for i in range(1,11):
        lock.acquire()
        print(i,end=" ")
        lock.release()
        sleep(0.5)
    return
def main():
    t1 = Thread(target=count, args=())
    t2 = Thread(target=count, args=())
    t3 = Thread(target=count, args=())
    t4 = Thread(target=count, args=())
    t5 = Thread(target=count, args=())
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    return
if __name__ =="__main__":
    main()