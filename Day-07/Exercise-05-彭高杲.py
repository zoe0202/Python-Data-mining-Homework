#1. 将Day02中计算有效互动比的方法写为函数

def interactive_rate():
    number_fans = float(input('Please write the number of fans there: '))
    number_interaction = float(input('The number of interaction: '))
    rate = str(round(number_interaction/number_fans,3))
    print('Efficient interactive rate is '+rate)

interactive_rate()

#2. 使用迭代的方法实现菲波那切数列的计算

if __name__ == "__main__":
    def fib(i):
        a,b = 0,1
        for i in range(i+1):
            a,b = b, a+b
        return a

    num = int(input('Please input the integer there: '))
    for q in range(num):
        print(fib(q),end=',')