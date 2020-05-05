fans = float(input("请输入粉丝量："))
interaction = float(input("请输入互动量："))
validity = interaction / fans
print("有效互动比为：%0.1f" % validity)
