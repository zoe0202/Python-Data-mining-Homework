list0 = input('请输入列表：').split()
list1 = [int(list0[i]) for i in range(len(list0))]
list2 = [str(i) for i in list1]
list3 = ','.join(list2)
print('列表为：')
print(list1)
print('字符串为：')
print(list3)
