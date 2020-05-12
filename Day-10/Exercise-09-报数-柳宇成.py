from threading import Thread, Lock
from time import time, sleep
import threading


def run(n):
    i = 1
    for i in range(1, 11):
        mutex.acquire()
        print('%s:%s\n' % (n, i))
        mutex.release()
        i += 1
        sleep(0.5)


mutex = threading.Lock()


def main():
    task1 = Thread(target=run, args=("task1",))
    task2 = Thread(target=run, args=("task2",))
    task3 = Thread(target=run, args=("task3",))
    task4 = Thread(target=run, args=("task4",))
    task5 = Thread(target=run, args=("task5",))
    task1.start()
    task2.start()
    task3.start()
    task4.start()
    task5.start()


''' task1 = NumberOff('task1')

 task2 = NumberOff('task2')

 task3 = NumberOff('task3')

 task4 = NumberOff('task4')

 task5 = NumberOff('task5')'''

if __name__ == '__main__':
    main()
