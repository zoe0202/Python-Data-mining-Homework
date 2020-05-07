def ratio(interaction, fans):
    validity = interaction / fans
    return validity


a = int(input('请输入粉丝数：'))
b = int(input('请输入互动数：'))

print('有效互动数为：%d' % ratio(b, a))
