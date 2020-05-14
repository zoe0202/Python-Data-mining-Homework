import threading
from time import time, sleep

def count():
    for counter in range(1, 11):
        print(counter)
        sleep(0.5)
        counter += 1


def main():
    start = time()
    threads = []
    for i in range(5):
       t = threading.Thread(target=count, args=())
    threads.append(t)
    for i in threads:
        i.start()
        i.join()
    print('报数结束')

    end = time()
    print('总共耗费了%d秒' % (end - start))

if __name__ == '__main__':
    main()