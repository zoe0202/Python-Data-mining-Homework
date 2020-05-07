def count(fans,interaction):
    ratio=interaction/fans
    return ratio
interaction=int(input("请输入互动值"))
fans=int(input("请输入粉丝量"))
print("互动比为："，count(fans,interaction))

