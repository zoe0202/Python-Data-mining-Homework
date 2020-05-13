'''
-*- coding: utf-8 -*-
@Author  : liuyuxuan
多线程报数
'''
from threading import Thread, Lock
from time import sleep

counter = 0


def count_off(lock):
    lock.acquire()
    global counter
    if counter < 5:
        try:
            counter += 1
            print(counter)
            count_time = 0.5
            sleep(count_time)
        finally:
            lock.release()


def main():
    lock = Lock()
    threads = []
    for _ in range(10):
        t = Thread(target=count_off, args=(lock,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
