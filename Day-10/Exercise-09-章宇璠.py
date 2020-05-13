import threading
from time import time, sleep

def count():
    for i in range(1, 11):
        print(i)
        sleep(0.5)

def main():
    start = time()
    added_thread = threading.Thread(target=count)
    thread2 = threading.Thread(target=count)
    thread3 = threading.Thread(target=count)
    thread4 = threading.Thread(target=count)
    thread5 = threading.Thread(target=count)
    added_thread.start()
    added_thread.join()
    print('报数结束')

    end = time()
    print('总共耗费了%d秒' % (end - start))

if __name__ == '__main__':
    main() 