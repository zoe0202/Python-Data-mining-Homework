if __name__ == "__main__":
    x = int(input('x = '))
    y = int(input('y = '))
    if x > y:
        x, y = y, x
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0 and factor== 1:
               print('%d和%d是互质数' % (x, y))
        else:
            print('%d和%d不是互质数' % (x, y))
            break
