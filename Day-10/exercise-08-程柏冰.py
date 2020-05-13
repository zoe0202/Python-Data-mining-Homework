#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import threading

def test():
    for i in range(1, 11):
        time.sleep(0.5)
        print(i)

def main():
    added_thread = threading.Thread(target=test)
    thread2 = threading.Thread(target=test)
    thread3 = threading.Thread(target=test)
    thread4 = threading.Thread(target=test)
    thread5 = threading.Thread(target=test)
    added_thread.start()
    added_thread.join()
    print('all done')

if __name__ == '__main__':
    main()