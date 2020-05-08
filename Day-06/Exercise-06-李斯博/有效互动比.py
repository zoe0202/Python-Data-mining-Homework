def Interaction(m,n):
    Effective_interaction_ratio=m/n
    return Effective_interaction_ratio

Interaction_quantity=float(input('请输入互动量='))
Number_of_followers=float(input('请输入粉丝量='))
c=Interaction(Interaction_quantity,Number_of_followers)
print('有效互动比是',c)