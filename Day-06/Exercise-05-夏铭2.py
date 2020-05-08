def is_Fibonacci(n):
  a, b = 0, 1
  for i in range(n + 1):
    a, b = b, a + b
  return a

x=int(input('请输入项数'))
for i in range(x):
  print(is_Fibonacci(i))