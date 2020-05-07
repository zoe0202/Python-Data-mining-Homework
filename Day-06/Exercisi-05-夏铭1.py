def count(fans,interaction):
    '''
    计算有效互动比
    fans:粉丝数
    interaction:互动量
    '''
    ratio=interaction/fans
    return ratio
interaction=int(input('请输入互动量'))
fans=int(input('请输入粉丝数'))
print(count(fans,interaction))
