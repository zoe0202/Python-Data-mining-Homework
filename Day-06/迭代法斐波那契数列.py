def fib(max):
	i,a,b = 0,0,1
	while i < max:
		yield b
		a,b = b,a+b
		i += 1