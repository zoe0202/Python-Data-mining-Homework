a = int(input('ゼロ以外の自然数を入力してください '))
b = int(input('ゼロ以外の自然数を入力してください，もう一つ'))
# 请输入非零自然数 和 请输入另一个非零自然数
if a > b:
    a,b = b,a
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print('それらの最大公約数は'+str(factor))
        if factor == 1:
            print('それらは互質数です')
            #它们是互质数
        else:
            print('それらは互質数ではありません')
            # 它们不是互质数
            break


