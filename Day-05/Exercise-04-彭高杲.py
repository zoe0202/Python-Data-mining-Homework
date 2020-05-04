#1. 根据用户输入的文件名，返回文件的后缀名
name = input("Please write your document's name there: ")
name = [name]
for y in (x.split('.') for x in name):
    print(y[1])

#2. 将列表转换为字符串，并使用逗号分隔列表中的各个元素
liebiao = [str(i) for i in input("Please write your liebiao there: ").split()]
x = ''
for y in liebiao:
    x += y+','
print(x[:-1])