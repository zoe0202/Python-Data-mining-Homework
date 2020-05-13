from threading import Thread
from time import time, sleep


def count10 ():
    current_num = 0
    for i in range(1, 11):
        current_num = i
        print(current_num)
        sleep(0.5)

def main():
    start = time()
    t1 = Thread(target=count10, args=())
    t1.start()
    t2 = Thread(target=count10, args=())
    t2.start()
    t3 = Thread(target=count10, args=())
    t3.start()
    t4 = Thread(target=count10, args=())
    t4.start()
    t5 = Thread(target=count10, args=())
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()