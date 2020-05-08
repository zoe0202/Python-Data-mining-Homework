'''
迭代实现菲波那切数列
'''
def fibs(n):
    result = [1, 1]
    for i in range(n - 2):#迭代循环
        result.append(result[-2] + result[-1])
    return result

print (fibs(15))