import time
x=time.time()
y=time.localtime(x)
z=time.strftime('%Y-%m-%d',y)
time.sleep(1)
print('时间是')
print(z)