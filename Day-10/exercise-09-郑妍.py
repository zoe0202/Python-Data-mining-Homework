from threading import Thread
from time import sleep


def count():
    for i in range(1,11):
        print(i)
        sleep(0.5)


def main():
    count1 = Thread(target=count, args=())
    count1.start()
    count2 = Thread(target=count, args=())
    count2.start()
    count3 = Thread(target=count, args=())
    count3.start()
    count4 = Thread(target=count, args=())
    count4.start()
    count5 = Thread(target=count, args=())
    count5.start()
    count1.join()
    count2.join()
    count3.join()
    count4.join()
    count5.join()


if __name__ == '__main__':
    main()
