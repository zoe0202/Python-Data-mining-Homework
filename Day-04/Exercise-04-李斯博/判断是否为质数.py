''''''
'判断是否为质数'
'Author：李斯博'
''''''

x = int(input())
isprime = False
for K in range(2, x):
  if x % K == 0:
     break
  else:
    isprime = True
  if isprime:
    print('is prime')
  else:
    print('is not prime')
