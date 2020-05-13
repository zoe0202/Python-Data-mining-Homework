import threading
import time

number=[1,2,3,4,5,6,7,8,9,10]
def count_off():
    for i in number:
        time.sleep(0.5)
        print(i)


def main():
    t1 = threading.Thread(target=count_off)
    t1.start()
    t2 = threading.Thread(target=count_off)
    t2.start()
    t3 = threading.Thread(target=count_off)
    t3.start()
    t4 = threading.Thread(target=count_off)
    t4.start()
    t5 = threading.Thread(target=count_off)
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

if __name__ == '__main__':
    main()


