#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import threading

def test():
    for i in range(1, 11):
        time.sleep(0.5)
        print(threading.current_thread().name +':'+str(i))

def main():
    thread1 = threading.Thread(target=test)
    thread1.start()
    thread2 = threading.Thread(target=test)
    thread2.start()
    thread3 = threading.Thread(target=test)
    thread3.start()
    thread4 = threading.Thread(target=test)
    thread4.start()
    thread5 = threading.Thread(target=test)
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print('all done')

if __name__ == '__main__':
    main()