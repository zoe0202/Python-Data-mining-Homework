from threading import Thread
from time import sleep
def print_number():
    count=0
    for i in range(1,11):
        print(i)
        sleep(0.5)
        count+=1
def main():
    start = print_number()
    t1 = Thread(target=print_number())
    t1.start()
    t2 = Thread(target=print_number())
    t2.start()
    t3 = Thread(target=print_number())
    t3.start()
    t4 = Thread(target=print_number())
    t4.start()
    t5 = Thread(target=print_number())
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

if __name__ == '__main__':
    main()