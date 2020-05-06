def func(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)


res = func(3)
print(res)
