def fib(n):
	n1=1
	n2=1
	n3=1
	if n < 1:
		print('input error')
	while (n-2) > 0:
		n3=n2+n1
		n1=n2
		n2=n3
		n -= 1
#前面的部分都是循环，输入值循环完毕会进行下一个输入值，之所以有这个n-=1，是控制其循环次数，循环1次是2，循环2次是3，以此类推。因为初始值你呢那都是不变的。
	return n3
for n in range(1,10):
	print(fib(n),end=',')
